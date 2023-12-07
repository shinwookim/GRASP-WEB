from flask import render_template, redirect, url_for, flash, request, jsonify, current_app
from app.results import bp
from app.results import report
from app.models.result import Result
from app.extensions import db

@bp.route("/") # Decorator for the index function, which is the view function for the index page
def index(): # View function for the index page
    return render_template("results/results.html") # Render the results template, which will fill any jinja2 template tags with the values provided in the render_template function call

@bp.route("/history")
def history():
    results = Result.query.all()
    return render_template("results/history.html", results=results)

# @bp.route("/history/<filename>")
# def history_file(filename):
#     return render_template("results/history_file.html", filename=filename)