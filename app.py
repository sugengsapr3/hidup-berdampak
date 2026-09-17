"""
Website brand "HIDUP. BERDAMPAK".
Ecosystem edukasi, pengembangan diri, kepemimpinan, dan dampak.
Dibangun dengan Python + Flask.

Menjalankan:
    pip install -r requirements.txt
    python app.py
Lalu buka http://127.0.0.1:5000
"""
import os
import secrets
from datetime import datetime

from flask import (
    Flask, render_template, request, abort, flash, redirect, url_for, session,
    make_response,
)
from itsdangerous import URLSafeSerializer, BadSignature
from authlib.integrations.flask_client import OAuth

import uuid

import data
import db
import payments

app = Flask(__name__)
# Secret key dari environment (fallback untuk dev lokal saja).
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-ganti-di-produksi")

# Konfigurasi cookie session agar andal saat alur OAuth (kembali dari Google).
# SameSite=Lax + Secure diperlukan supaya cookie 'state' OAuth tetap terbaca
# saat callback di lingkungan HTTPS/serverless (Vercel).
app.config.update(
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
)

# --- Konfigurasi OAuth Google -----------------------------------------
# Client ID & Secret diambil dari environment variable (tidak di-hardcode),
# sehingga aman di repo publik. Set di Vercel (SEMUA environment):
# GOOGLE_CLIENT_ID & GOOGLE_CLIENT_SECRET.
GOOGLE_CLIENT_ID = (os.environ.get("GOOGLE_CLIENT_ID") or "").strip()
GOOGLE_CLIENT_SECRET = (os.environ.get("GOOGLE_CLIENT_SECRET") or "").strip()

oauth = OAuth(app)
if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    oauth.register(
        name="google",
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={
            "scope": "openid email profile",
            "token_endpoint_auth_method": "client_secret_post",
        },
    )


def google_enabled():
    return bool(GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET)


@app.context_processor
def inject_globals():
    """Data yang dipakai di semua template (navbar, footer)."""
    return {
        "site": data.SITE,
        "nav": data.NAV,
        "learn_topics": data.LEARN_TOPICS,
        "nav_business_items": data.NAV_BUSINESS_ITEMS,
        "nav_resources_items": data.NAV_RESOURCES_ITEMS,
        "footer_columns": data.FOOTER_COLUMNS,
        "current_year": datetime.now().year,
        "current_user": session.get("user"),
    }


# ---------------------------------------------------------------- Beranda
@app.route("/")
def home():
    return render_template(
        "home.html",
        learn_topics=data.LEARN_TOPICS,
        featured=data.FEATURED,
        book=data.BOOKS[0],
        active="home",
    )


# ---------------------------------------------------------------- Belajar
@app.route("/belajar")
def learn():
    return render_template("learn.html", topics=data.LEARN_TOPICS, active="learn")


@app.route("/belajar/<slug>")
def learn_detail(slug):
    topic = next((t for t in data.LEARN_TOPICS if t["slug"] == slug), None)
    if topic is None:
        abort(404)
    return render_template("learn_detail.html", topic=topic, active="learn")


# ---------------------------------------------------------------- Untuk Bisnis
@app.route("/untuk-bisnis")
def business():
    return render_template(
        "business.html",
        hero=data.BUSINESS_HERO,
        services=data.BUSINESS_SERVICES,
        capabilities=data.BUSINESS_CAPABILITIES,
        active="business",
    )


# ---------------------------------------------------------------- Buku
@app.route("/buku")
def books():
    return render_template("books.html", books=data.BOOKS, active="books")


@app.route("/buku/<slug>")
def book_detail(slug):
    book = next((b for b in data.BOOKS if b["slug"] == slug), None)
    if book is None:
        abort(404)
    return render_template("book_detail.html", book=book, active="books")


# ---------------------------------------------------------------- Sumber Daya
@app.route("/sumber-daya")
def resources():
    return render_template("resources.html", resources=data.RESOURCES, active="resources")


# ---------------------------------------------------------------- Tentang
@app.route("/tentang")
def about():
    return render_template("about.html", philosophy=data.PHILOSOPHY, active="about")


# ---------------------------------------------------------------- Login
@app.route("/login")
def login():
    return render_template(
        "login.html",
        providers=data.AUTH_PROVIDERS,
        google_enabled=google_enabled(),
        active="login",
    )


# ---------------------------------------------------------------- OAuth Google
# Nama cookie khusus untuk menyimpan state OAuth (terpisah dari session Flask).
OAUTH_STATE_COOKIE = "g_oauth_state"


def _state_serializer():
    return URLSafeSerializer(app.secret_key, salt="oauth-state")


@app.route("/auth/google")
def auth_google():
    if not google_enabled():
        flash("Login Google belum dikonfigurasi. Coba lagi nanti.", "error")
        return redirect(url_for("login"))

    # Buat state acak sendiri; JANGAN mengandalkan session Flask (rapuh di serverless).
    state = secrets.token_urlsafe(24)
    redirect_uri = url_for("auth_google_callback", _external=True)

    # Bangun URL otorisasi Google secara manual dengan state kita.
    metadata = oauth.google.load_server_metadata()
    auth_endpoint = metadata["authorization_endpoint"]
    params = {
        "response_type": "code",
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "scope": "openid email profile",
        "state": state,
        "prompt": "select_account",
    }
    from urllib.parse import urlencode
    auth_url = f"{auth_endpoint}?{urlencode(params)}"

    # Simpan state di cookie terpisah yang ditandatangani (bertahan antar-invocation).
    resp = make_response(redirect(auth_url))
    signed = _state_serializer().dumps(state)
    resp.set_cookie(
        OAUTH_STATE_COOKIE, signed,
        max_age=600, httponly=True, secure=True, samesite="Lax",
    )
    return resp


@app.route("/auth/google/callback")
def auth_google_callback():
    if not google_enabled():
        abort(404)
    if request.args.get("error"):
        flash("Login Google dibatalkan.", "error")
        return redirect(url_for("login"))

    # Verifikasi state: bandingkan query 'state' dengan cookie bertanda tangan.
    returned_state = request.args.get("state", "")
    signed_cookie = request.cookies.get(OAUTH_STATE_COOKIE, "")
    try:
        expected_state = _state_serializer().loads(signed_cookie)
    except BadSignature:
        expected_state = None
    if not returned_state or returned_state != expected_state:
        app.logger.error("OAuth state mismatch (cookie hilang/berbeda).")
        flash("Sesi login kedaluwarsa. Silakan coba lagi.", "error")
        return redirect(url_for("login"))

    code = request.args.get("code")
    if not code:
        flash("Gagal masuk dengan Google. Silakan coba lagi.", "error")
        return redirect(url_for("login"))

    try:
        # Tukar authorization code -> token via requests langsung ke token endpoint,
        # menyertakan client_id & client_secret secara eksplisit (client_secret_post).
        import requests as _requests
        metadata = oauth.google.load_server_metadata()
        token_endpoint = metadata["token_endpoint"]
        redirect_uri = url_for("auth_google_callback", _external=True)
        token_resp = _requests.post(
            token_endpoint,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": redirect_uri,
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
            },
            timeout=15,
        )
        if token_resp.status_code != 200:
            app.logger.error("Token endpoint %s: %s", token_resp.status_code, token_resp.text)
            flash("Gagal masuk dengan Google. Silakan coba lagi.", "error")
            return redirect(url_for("login"))
        access_token = token_resp.json().get("access_token")
        # Ambil profil user dari endpoint userinfo memakai access token.
        info_resp = _requests.get(
            "https://openidconnect.googleapis.com/v1/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=15,
        )
        info = info_resp.json()
    except Exception as e:
        app.logger.error("OAuth token exchange gagal: %s", repr(e))
        flash("Gagal masuk dengan Google. Silakan coba lagi.", "error")
        return redirect(url_for("login"))

    if not info.get("email"):
        flash("Tidak bisa membaca data akun Google.", "error")
        return redirect(url_for("login"))

    session["user"] = {
        "name": info.get("name", info["email"].split("@")[0]),
        "email": info["email"],
        "picture": info.get("picture", ""),
    }
    # Simpan/update user ke database (jika DB tersedia). Jangan gagalkan login
    # kalau DB bermasalah, cukup catat error.
    if db.db_enabled():
        try:
            db.upsert_user(
                session["user"]["email"],
                session["user"]["name"],
                session["user"]["picture"],
            )
        except Exception as e:
            app.logger.error("Gagal simpan user ke DB: %s", repr(e))
    # Hapus cookie state yang sudah dipakai.
    resp = make_response(redirect(url_for("account")))
    resp.delete_cookie(OAUTH_STATE_COOKIE)
    flash(f"Selamat datang, {session['user']['name']} 👋", "success")
    return resp


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Kamu sudah keluar.", "success")
    return redirect(url_for("home"))


@app.route("/akun")
def account():
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))
    owned = []
    if db.db_enabled():
        try:
            owned = db.my_courses(user["email"])
        except Exception as e:
            app.logger.error("Gagal ambil kelas user: %s", repr(e))
    return render_template("account.html", owned=owned, active="")


# ---------------------------------------------------------------- Kelas (berbayar)
@app.route("/kelas")
def courses():
    items = db.list_courses() if db.db_enabled() else []
    return render_template("courses.html", courses=items, active="courses")


@app.route("/kelas/<slug>")
def course_detail(slug):
    course = db.get_course(slug) if db.db_enabled() else None
    if not course:
        abort(404)
    user = session.get("user")
    owned = bool(user) and db.has_access(user["email"], slug)
    return render_template(
        "course_detail.html", course=course, owned=owned, active="courses"
    )


@app.route("/kelas/<slug>/beli", methods=["POST"])
def course_buy(slug):
    """Mulai pembelian kelas.

    - Jika Midtrans aktif: buat order (pending) + transaksi Snap, arahkan user
      ke halaman pembayaran Midtrans. Akses diberikan lewat webhook setelah bayar.
    - Jika Midtrans belum dikonfigurasi: fallback beri akses langsung (mode uji),
      supaya alur tetap bisa dicoba sebelum key pembayaran dipasang.
    """
    user = session.get("user")
    if not user:
        return redirect(url_for("login"))
    course = db.get_course(slug) if db.db_enabled() else None
    if not course:
        abort(404)

    # Fallback mode uji (belum ada Midtrans): beri akses langsung.
    if not payments.is_enabled():
        try:
            db.enroll(user["email"], slug, status="paid")
            flash(f"(Mode uji) Kamu sekarang punya akses ke \u201c{course['title']}\u201d.", "success")
        except Exception as e:
            app.logger.error("Gagal enroll (mode uji): %s", repr(e))
            flash("Terjadi kesalahan. Coba lagi.", "error")
        return redirect(url_for("course_detail", slug=slug))

    # Mode pembayaran sungguhan (Midtrans Snap).
    order_id = f"HB-{slug[:12]}-{uuid.uuid4().hex[:10]}"
    amount = int(course["price"])
    try:
        db.create_order(order_id, user["email"], slug, amount, status="pending")
    except Exception as e:
        app.logger.error("Gagal buat order: %s", repr(e))
        flash("Terjadi kesalahan. Coba lagi.", "error")
        return redirect(url_for("course_detail", slug=slug))

    redirect_url, err = payments.create_snap_transaction(
        order_id, amount, course["title"], user["email"], user["name"]
    )
    if err:
        app.logger.error("Midtrans gagal: %s", err)
        flash("Gagal memulai pembayaran. Coba lagi nanti.", "error")
        return redirect(url_for("course_detail", slug=slug))
    return redirect(redirect_url)


@app.route("/midtrans/notify", methods=["POST"])
def midtrans_notify():
    """Webhook dari Midtrans. Set order 'paid' dan beri akses bila pembayaran sukses."""
    payload = request.get_json(silent=True) or {}
    order_id = payload.get("order_id", "")
    status_code = payload.get("status_code", "")
    gross_amount = payload.get("gross_amount", "")
    signature = payload.get("signature_key", "")
    txn_status = payload.get("transaction_status", "")
    fraud = payload.get("fraud_status", "accept")

    if not payments.verify_signature(order_id, status_code, gross_amount, signature):
        app.logger.error("Webhook signature tidak valid untuk %s", order_id)
        abort(403)

    order = db.get_order(order_id)
    if not order:
        abort(404)

    if txn_status in ("capture", "settlement") and fraud == "accept":
        db.set_order_status(order_id, "paid")
        db.enroll(order["email"], order["course_slug"], status="paid")
    elif txn_status in ("cancel", "deny", "expire"):
        db.set_order_status(order_id, "failed")
    return "OK", 200


@app.route("/kelas/<slug>/selesai")
def course_finish(slug):
    """Halaman kembali setelah user menyelesaikan pembayaran di Midtrans."""
    course = db.get_course(slug) if db.db_enabled() else None
    if not course:
        abort(404)
    user = session.get("user")
    owned = bool(user) and db.has_access(user["email"], slug)
    return render_template(
        "course_finish.html", course=course, owned=owned, active="courses"
    )


@app.route("/kelas/<slug>/belajar")
def course_learn(slug):
    """Ruang belajar: hanya untuk user yang sudah punya akses (sudah bayar)."""
    course = db.get_course(slug) if db.db_enabled() else None
    if not course:
        abort(404)
    user = session.get("user")
    # Wajib login.
    if not user:
        flash("Silakan masuk untuk mengakses materi kelas.", "error")
        return redirect(url_for("login"))
    # Wajib punya akses (sudah bayar).
    if not db.has_access(user["email"], slug):
        flash("Kamu belum punya akses ke kelas ini.", "error")
        return redirect(url_for("course_detail", slug=slug))
    materials = data.COURSE_MATERIALS.get(slug, [])
    return render_template(
        "course_learn.html", course=course, materials=materials, active="courses"
    )


# ---------------------------------------------------------------- Pencarian
def _build_search_index():
    """Kumpulkan semua konten yang bisa dicari menjadi satu daftar seragam."""
    index = []
    for t in data.LEARN_TOPICS:
        index.append({
            "title": t["title"], "desc": t.get("desc", ""), "body": t.get("intro", ""),
            "kind": "Belajar", "url": url_for("learn_detail", slug=t["slug"]),
        })
    for b in data.BOOKS:
        if b["status"] == "available":
            index.append({
                "title": b["title"], "desc": b.get("blurb", ""), "body": b.get("desc", ""),
                "kind": "Buku", "url": url_for("book_detail", slug=b["slug"]),
            })
    for s in data.BUSINESS_SERVICES:
        index.append({
            "title": s["title"], "desc": s.get("desc", ""), "body": "",
            "kind": "Untuk Bisnis", "url": url_for("business"),
        })
    for r in data.RESOURCES:
        index.append({
            "title": r["title"], "desc": r.get("desc", ""), "body": "",
            "kind": "Sumber Daya", "url": url_for("resources"),
        })
    return index


@app.route("/cari")
def search():
    query = request.args.get("q", "").strip()
    results = []
    if query:
        q = query.lower()
        for item in _build_search_index():
            haystack = f"{item['title']} {item['desc']} {item['body']}".lower()
            if q in haystack:
                results.append(item)
    return render_template("search.html", query=query, results=results, active="")


# ---------------------------------------------------------------- Bergabung
@app.route("/bergabung", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        if not email:
            flash("Mohon isi alamat email kamu.", "error")
        else:
            flash(
                "Terima kasih sudah bergabung. Satu refleksi pilihan akan segera "
                "hadir di inbox-mu 🌱",
                "success",
            )
            return redirect(url_for("join"))
    return render_template("join.html", active="join")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", active=""), 404


if __name__ == "__main__":
    app.run(debug=True)
