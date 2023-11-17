from flask import render_template, redirect, url_for
from app.home import bp

@bp.route("/")
def index():
    return render_template("home/home.html")