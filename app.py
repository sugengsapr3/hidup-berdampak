"""
Website brand "HIDUP. BERDAMPAK".
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
    """Sisipkan data yang dipakai di semua template (navbar, footer)."""
    return {
        "site": data.SITE,
        "nav": data.NAV,
        "tutorial_topics": data.TUTORIAL_TOPICS,
        "current_year": datetime.now().year,
    }


@app.route("/")
def home():
    return render_template(
        "home.html",
        journeys=data.JOURNEYS,
        pillars=data.PILLARS,
        active="home",
    )


@app.route("/perjalanan")
def journeys():
    return render_template("journeys.html", journeys=data.JOURNEYS, active="journeys")


@app.route("/perjalanan/<slug>")
def journey_detail(slug):
    journey = next((j for j in data.JOURNEYS if j["slug"] == slug), None)
    if journey is None:
        abort(404)
    return render_template("journey_detail.html", journey=journey, active="journeys")


@app.route("/tentang")
def about():
    return render_template("about.html", pillars=data.PILLARS, active="about")


@app.route("/kelas")
def courses():
    return render_template("courses.html", courses=data.COURSES, active="courses")


@app.route("/kelas/<slug>")
def course_detail(slug):
    course = next((c for c in data.COURSES if c["slug"] == slug), None)
    if course is None:
        abort(404)
    return render_template("course_detail.html", course=course, active="courses")


@app.route("/untuk-bisnis")
def business():
    return render_template("business.html", offers=data.BUSINESS_OFFERS, active="business")


@app.route("/tutorial")
def tutorials():
    return render_template("tutorials.html", topics=data.TUTORIAL_TOPICS, active="tutorials")


@app.route("/tutorial/<slug>")
def tutorial_detail(slug):
    topic = next((t for t in data.TUTORIAL_TOPICS if t["slug"] == slug), None)
    if topic is None:
        abort(404)
    return render_template("tutorial_detail.html", topic=topic, active="tutorials")


@app.route("/sumber-daya")
def resources():
    return render_template("resources.html", resources=data.RESOURCES, active="resources")


@app.route("/login")
def login():
    return render_template("login.html", active="login")


def _build_search_index():
    """Kumpulkan semua konten yang bisa dicari menjadi satu daftar seragam."""
    index = []
    for j in data.JOURNEYS:
        index.append({
            "title": j["title"], "desc": j.get("desc", ""), "body": j.get("body", ""),
            "kind": "Perjalanan", "url": url_for("journey_detail", slug=j["slug"]),
        })
    for c in data.COURSES:
        index.append({
            "title": c["title"], "desc": c.get("desc", ""), "body": c.get("intro", ""),
            "kind": "Kelas", "url": url_for("course_detail", slug=c["slug"]),
        })
    for t in data.TUTORIAL_TOPICS:
        index.append({
            "title": t["title"], "desc": t.get("desc", ""), "body": t.get("intro", ""),
            "kind": "Tutorial", "url": url_for("tutorial_detail", slug=t["slug"]),
        })
    for r in data.RESOURCES:
        index.append({
            "title": r["title"], "desc": r.get("desc", ""), "body": "",
            "kind": "Sumber Daya", "url": url_for("resources"),
        })
    for o in data.BUSINESS_OFFERS:
        index.append({
            "title": o["title"], "desc": o.get("desc", ""), "body": "",
            "kind": "Untuk Bisnis", "url": url_for("business"),
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


@app.route("/bergabung", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        if not name or not email:
            flash("Mohon isi nama dan email kamu.", "error")
        else:
            flash(
                f"Selamat datang di gerakan HIDUP. BERDAMPAK, {name}. "
                "Mari tinggalkan sesuatu yang berarti 🌱",
                "success",
            )
            return redirect(url_for("join"))
    return render_template("join.html", active="join")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", active=""), 404


if __name__ == "__main__":
    app.run(debug=True)
