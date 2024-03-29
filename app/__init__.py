import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config : str):

    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), "config", f"{config}.py")
    app.config.from_pyfile(configuration)

    db.init_app(app)

    return app