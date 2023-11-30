from flask import render_template, redirect, url_for
from app.home import bp
from app.extensions import db
from app.models import result

@bp.route("/") # Decorator for the index function, which is the view function for the index page
def index(): # View function for the index page
    db.create_all()
    return render_template("home/home.html") # Render the home template (home.html), which will fill any jinja2 template tags with the values provided in the render_template function call