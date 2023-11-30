from flask import render_template, redirect, url_for
from app.results import bp

@bp.route("/") # Decorator for the index function, which is the view function for the index page
def index(): # View function for the index page
    return render_template("results/results.html") # Render the results template, which will fill any jinja2 template tags with the values provided in the render_template function call

# @bp.route("/history")
# def history():
#     return render_template("results/history.html")