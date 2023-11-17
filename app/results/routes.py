from flask import render_template, redirect, url_for
from app.results import bp

@bp.route("/")
def index():
    return render_template("results/results.html")