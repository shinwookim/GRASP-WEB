from flask import Blueprint # Import flask Blueprint class for the blueprint object

bp = Blueprint("home", __name__) # Create a blueprint object for the home blueprint, with the name "home"

from app.home import routes # Import the routes module from the home package