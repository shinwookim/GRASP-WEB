from flask import Blueprint # Import flask Blueprint class for the blueprint object

bp = Blueprint("acknowledgements", __name__) # Create a blueprint object for the experiment blueprint, with the name "experiment"

from app.acknowledgements import routes # Import the routes module from the experiment package