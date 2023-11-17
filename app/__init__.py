from flask import Flask

from config import Config

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize any extensions here

    # Register blueprints here
    from app.home import bp as home_bp
    app.register_blueprint(home_bp, url_prefix = "/") # Register the home blueprint with the app, with the url prefix "/"

    from app.experiment import bp as experiment_bp
    app.register_blueprint(experiment_bp, url_prefix = "/experiment") # Register the experiment blueprint with the app, with the url prefix "/experiment"

    from app.results import bp as results_bp
    app.register_blueprint(results_bp, url_prefix = "/results") # Register the results blueprint with the app, with the url prefix "/results"

    from app.acknowledgements import bp as acknowledgements_bp
    app.register_blueprint(acknowledgements_bp, url_prefix = "/acknowledgements") # Register the results blueprint with the app, with the url prefix "/acknowledgements"

    '''
    url_prefix is mainly used for jinja2 url_for() function, 
    which generates a URL to the given endpoint with the method provided.
    
    For example, url_for("results.index") will return "/results/" instead of 
    "/".
    '''

    return app