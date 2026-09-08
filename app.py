"""
Website brand "HIDUP. BERDAMPAK".
Ecosystem edukasi, pengembangan diri, kepemimpinan, dan dampak.
Dibangun dengan Python + Flask.

Menjalankan:
    pip install -r requirements.txt
    python app.py
Lalu buka http://127.0.0.1:5000
"""
from datetime import datetime

from flask import Flask, render_template, request, abort, flash, redirect, url_for

import data

app = Flask(__name__)
app.secret_key = "ganti-dengan-secret-key-anda"


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
    return render_template("login.html", providers=data.AUTH_PROVIDERS, active="login")


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
