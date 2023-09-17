from app.models import db
from app.auth import login_manager
import os

import click
from flask import Flask
from flask_assets import Environment, Bundle

template_dir = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'templates')


class DatabaseSettings:
    def __init__(self, env='production') -> None:
        if env == 'production':
            self.HOST = 'db'
            self.PORT = 5432

        self.NAME = os.getenv('POSTGRES_NAME', 'postgres')
        self.USER = os.getenv('POSTGRES_USER', 'postgres')
        self.PASSWORD = os.getenv('POSTGRES_PASS', '7xyed8uDyi0=')
        self.URL = f'postgresql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}'


def create_app():
    app = Flask(__name__)

    from . import main, auth, webhook, commands

    assets = Environment(app)
    assets.url = app.static_url_path
    styles = Bundle('css/*.scss', filters='pyscss', output='css/styles.css')
    js = Bundle('js/*.js', filters='jsmin', output='js/bundle.js')
    assets.register('scss_all', styles)
    assets.register('js_all', js)

    app.register_blueprint(main.blueprint)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(webhook.blueprint)
    app.register_blueprint(commands.extended_cli_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseSettings().URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.getenv('SECRET_KEY')

    db.init_app(app)
    login_manager.init_app(app)

    return app
