from flask import render_template, redirect, url_for
from app.acknowledgements import bp

@bp.route("/") # Decorator for the index function, which is the view function for the index page
def index(): # View function for the index page
    return render_template("acknowledgements/acknowledgements.html")