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
