from flask import Blueprint # Import flask Blueprint class for the blueprint object

bp = Blueprint("results", __name__) # Create a blueprint object for the results blueprint, with the name "results"

from app.results import routes # Import the routes module from the results package