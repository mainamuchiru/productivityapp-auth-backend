from flask import Flask
from .config import db, bcrypt, migrate
from .routes import register_routes

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "change-this-secret-key"

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)

register_routes(app)