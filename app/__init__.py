
from flask import Flask

# local imports
from config import app_config

__version__ = "v0.0.1"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
