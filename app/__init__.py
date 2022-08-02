
from flask import Flask
from logging.handlers import RotatingFileHandler
import os

# local imports
from config import app_config

__version__ = "v0.0.1"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # inject version var into all pages for footer
    @app.context_processor
    def injectVersion():
        return dict(version=__version__)

    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/neptune.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s %(name)s: %(message)s'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Neptune startup')

    return app

