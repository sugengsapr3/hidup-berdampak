"""Isolated English Learning Center prototype; browser-local progress."""
from flask import Blueprint, render_template
bp = Blueprint("english_center", __name__, url_prefix="/english")
@bp.get("/")
def dashboard():
    return render_template("english_center.html")
