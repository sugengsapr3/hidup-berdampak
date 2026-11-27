"""Checkout dan akses Daily Habit Tracker melalui verifikasi email."""
import base64
import hmac
import re
import secrets
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

from flask import Blueprint, abort, current_app, make_response, redirect, render_template, request, session, url_for

import db
import emails

bp = Blueprint("habit_checkout", __name__, url_prefix="/sumber-daya/daily-habit-tracker")
FILENAME = "daily-habit-tracker-hidup-berdampak.xlsx"
PUBLIC_ORIGIN = "https://hidupberdampak.vercel.app"


def tracker_file():
    return (Path(current_app.root_path) / "product_files" / FILENAME).read_bytes()


def render_step(step, status=200, **context):
    token = session.setdefault("habit_csrf", secrets.token_urlsafe(32))
    response = make_response(render_template("habit_checkout.html", step=step, csrf=token, **context), status)
    response.headers["Cache-Control"] = "no-store"
    response.headers["Referrer-Policy"] = "no-referrer"
    return response


def require_csrf():
    token = session.get("habit_csrf")
    supplied = request.form.get("csrf", "")
    if not token or not hmac.compare_digest(token.encode(), supplied.encode()):
        abort(400)


def prepare_storage(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS habit_tracker_claims (
            id text PRIMARY KEY,
            email text NOT NULL,
            created_at timestamptz NOT NULL DEFAULT now(),
            otp_hash text,
            otp_sent_at timestamptz,
            otp_sends integer NOT NULL DEFAULT 0,
            attempts integer NOT NULL DEFAULT 0
        )
    """)


def digest(claim_id, code):
    return hmac.digest(current_app.secret_key.encode(), f"{claim_id}:{code}".encode(), "sha256").hex()


def access_link(claim_id):
    return PUBLIC_ORIGIN + url_for(".product", claim_id=claim_id)


@bp.route("", methods=["GET", "POST"])
def checkout():
    if request.method == "GET":
        return render_step("checkout")
    require_csrf()
    name = request.form.get("name", "").strip()
    phone = re.sub(r"[ ()-]", "", request.form.get("phone", ""))
    email = request.form.get("email", "").strip().lower()
    confirm = request.form.get("confirm", "").strip().lower()
    values = {"name": name, "phone": phone, "email": email, "confirm": confirm}
    if not (
        2 <= len(name) <= 100
        and re.fullmatch(r"(?:\+62|62|0)?[0-9]{8,13}", phone)
        and len(email) <= 254
        and re.fullmatch(r"[^@\s<>]+@[^@\s<>]+\.[^@\s<>]+", email)
        and email == confirm
    ):
        return render_step("checkout", 400, values=values, error="Periksa nama, nomor HP, dan pastikan kedua alamat email sama.")
    if not db.db_enabled() or not emails.emails_enabled() or current_app.secret_key == "dev-secret-ganti-di-produksi":
        return render_step("checkout", 503, values=values, error="Layanan pengiriman email sedang tidak tersedia.")

    with db._conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT pg_advisory_xact_lock(1971001)")
        prepare_storage(cur)
        cur.execute("DELETE FROM habit_tracker_claims WHERE created_at < now() - interval '30 days'")
        cur.execute("""
            SELECT count(*), count(*) FILTER (WHERE email = %s)
            FROM habit_tracker_claims WHERE created_at > now() - interval '1 hour'
        """, (email,))
        total, recipient = cur.fetchone()
        if total >= 30 or recipient >= 3:
            return render_step("checkout", 429, values=values, error="Batas permintaan tercapai. Coba lagi nanti.")
        claim_id = secrets.token_urlsafe(24)
        cur.execute("INSERT INTO habit_tracker_claims (id, email) VALUES (%s, %s)", (claim_id, email))

    sent, _ = emails._send(
        email, "Konfirmasi klaim Daily Habit Tracker",
        f'<p>Halo {escape(name)},</p><p>Daily Habit Tracker kamu sudah siap.</p>'
        f'<p><a href="{access_link(claim_id)}">Akses Produk Digital</a></p>'
        '<p>Produk: Daily Habit Tracker<br>Total: Rp0<br>Metode: Klaim gratis</p>'
        '<p>HIDUP. BERDAMPAK</p>',
    )
    session["habit_confirmation"] = {"id": claim_id, "sent": sent}
    return redirect(url_for(".confirmation"), code=303)


@bp.get("/konfirmasi")
def confirmation():
    claim = session.get("habit_confirmation")
    if not claim:
        return redirect(url_for(".checkout"))
    return render_step("confirmation", claim_id=claim["id"], sent=claim["sent"])


@bp.route("/akses/<claim_id>", methods=["GET", "POST"])
def product(claim_id):
    if not re.fullmatch(r"[A-Za-z0-9_-]{32}", claim_id) or not db.db_enabled():
        abort(404)
    if request.method == "POST":
        require_csrf()
    verified = has_access(claim_id)
    action = request.form.get("action")
    now = datetime.now(timezone.utc)
    code = None
    error = None
    deliver = False
    with db._conn() as conn, conn.cursor() as cur:
        prepare_storage(cur)
        cur.execute("""
            SELECT email, otp_hash, otp_sent_at, otp_sends, attempts
            FROM habit_tracker_claims WHERE id = %s AND created_at > now() - interval '30 days'
            FOR UPDATE
        """, (claim_id,))
        claim = cur.fetchone()
        if not claim:
            abort(404)
        email, otp_hash, sent_at, sends, attempts = claim
        if not verified and action == "send":
            if sends >= 4:
                error = "Batas kirim kode untuk klaim ini tercapai."
            elif sent_at and now - sent_at < timedelta(minutes=1):
                error = "Tunggu 60 detik sejak pengiriman terakhir sebelum meminta kode baru."
            else:
                code = f"{secrets.randbelow(1_000_000):06d}"
                cur.execute("""
                    UPDATE habit_tracker_claims SET otp_hash = %s, otp_sent_at = %s,
                        otp_sends = otp_sends + 1, attempts = 0 WHERE id = %s
                """, (digest(claim_id, code), now, claim_id))
        elif not verified and action == "verify":
            entered = request.form.get("code", "").strip()
            if not otp_hash or not sent_at or now - sent_at >= timedelta(minutes=10) or attempts >= 5:
                error = "Kode sudah tidak berlaku. Minta kode baru."
            elif not re.fullmatch(r"[0-9]{6}", entered) or not hmac.compare_digest(otp_hash, digest(claim_id, entered)):
                cur.execute("UPDATE habit_tracker_claims SET attempts = attempts + 1 WHERE id = %s", (claim_id,))
                error = "Kode salah. Periksa email dan coba lagi."
            else:
                cur.execute("UPDATE habit_tracker_claims SET otp_hash = NULL, otp_sends = 0 WHERE id = %s", (claim_id,))
                session["habit_verified"] = {"id": claim_id, "until": int(now.timestamp()) + 86400}
                verified = deliver = True

    if code:
        ok, _ = emails._send(email, "Kode verifikasi HIDUP BERDAMPAK", f"<p>Kode verifikasi kamu: <strong>{code}</strong>.</p><p>Kode berlaku 10 menit.</p>")
        if not ok:
            error = "Kode belum berhasil dikirim. Coba kirim ulang setelah 60 detik."
        else:
            return redirect(url_for(".product", claim_id=claim_id), code=303)
    if deliver:
        ok, _ = emails._send(
            email, "File Daily Habit Tracker kamu",
            f'<p>Daily Habit Tracker terlampir. Kamu juga bisa <a href="{access_link(claim_id)}">buka halaman produk</a>.</p>',
            attachment={"filename": FILENAME, "content": base64.b64encode(tracker_file()).decode("ascii")},
        )
        session["habit_file_sent"] = ok
        return redirect(url_for(".product", claim_id=claim_id), code=303)
    if verified:
        return render_step("product", claim_id=claim_id, sent=session.get("habit_file_sent", False))
    local, domain = email.rsplit("@", 1)
    return render_step("verify", claim_id=claim_id, masked=f"{local[0]}***@{domain}", otp_ready=bool(otp_hash), error=error)


def has_access(claim_id):
    access = session.get("habit_verified", {})
    return access.get("id") == claim_id and access.get("until", 0) > datetime.now(timezone.utc).timestamp()


@bp.get("/akses/<claim_id>/unduh")
def download(claim_id):
    if not has_access(claim_id):
        return redirect(url_for(".product", claim_id=claim_id))
    response = make_response(tracker_file())
    response.headers.update({
        "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "Content-Disposition": f'attachment; filename="{FILENAME}"',
        "Cache-Control": "no-store",
    })
    return response
