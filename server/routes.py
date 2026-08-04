from flask import request, jsonify, session
from .models import User, Note
from .config import db
from .auth import login_required


def register_routes(app):

    @app.post("/signup")
    def signup():
        ...

    @app.post("/login")
    def login():
        ...

    @app.delete("/logout")
    def logout():
        ...

    @app.get("/me")
    def me():
        ...

    @app.get("/notes")
    @login_required
    def get_notes():
        ...

    @app.post("/notes")
    @login_required
    def create_note():
        ...