from flask import Flask

from .config import (
    db,
    bcrypt,
    migrate,
    SECRET_KEY,
    DATABASE_URL,
)

from .routes import register_routes


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)

    @app.get("/")
    def home():
        return {
            "message": "Welcome to the Productivity App Backend API"
        }, 200

    return app


app = create_app()