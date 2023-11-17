from flask import Flask

from config import Config

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize any extensions here

    # Register blueprints here
    from app.home import bp as home_bp
    app.register_blueprint(home_bp, url_prefix = "/")

    from app.experiment import bp as experiment_bp
    app.register_blueprint(experiment_bp, url_prefix = "/experiment")

    from app.results import bp as results_bp
    app.register_blueprint(results_bp, url_prefix = "/results")

    return app