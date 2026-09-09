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

import data

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
# sehingga aman di repo publik. Set di Vercel: GOOGLE_CLIENT_ID & GOOGLE_CLIENT_SECRET.
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")

oauth = OAuth(app)
if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    oauth.register(
        name="google",
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
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
        # Tukar authorization code -> token secara manual (tanpa cek session).
        redirect_uri = url_for("auth_google_callback", _external=True)
        token = oauth.google.fetch_access_token(
            redirect_uri=redirect_uri, code=code, grant_type="authorization_code",
        )
        # Ambil profil user dari endpoint userinfo memakai access token.
        resp = oauth.google.get(
            "https://openidconnect.googleapis.com/v1/userinfo", token=token
        )
        info = resp.json()
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
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template("account.html", active="")


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
