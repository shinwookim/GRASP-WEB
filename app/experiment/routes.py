from flask import render_template, redirect, url_for
from app.experiment import bp

@bp.route("/")
def index():
    return render_template("experiment/experiment.html")