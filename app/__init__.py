from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable Flask sessions
    app.secret_key = app.config["SECRET_KEY"]

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from app import models
    from app.routes import register_routes

    register_routes(app)

    return app