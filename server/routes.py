from flask import request, jsonify, session
from .models import User, Note
from .config import db
from .auth import login_required


def register_routes(app):

    # -------------------------
    # Authentication Routes
    # -------------------------

    @app.post("/signup")
    def signup():
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return jsonify({"error": "Username already exists"}), 409

        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        return jsonify(user.to_dict()), 201


    @app.post("/login")
    def login():
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            session["user_id"] = user.id
            return jsonify(user.to_dict()), 200

        return jsonify({"error": "Invalid username or password"}), 401


    @app.get("/me")
    def me():
        user_id = session.get("user_id")

        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401

        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify(user.to_dict()), 200


    @app.delete("/logout")
    def logout():
        session.pop("user_id", None)
        return {}, 204


    # -------------------------
    # Note Routes
    # -------------------------

    @app.get("/notes")
    @login_required
    def get_notes():

        page = request.args.get("page", 1, type=int)
        per_page = 5

        notes = (
            Note.query
            .filter_by(user_id=session["user_id"])
            .paginate(page=page, per_page=per_page, error_out=False)
        )

        return jsonify({
            "notes": [note.to_dict() for note in notes.items],
            "page": notes.page,
            "pages": notes.pages,
            "total": notes.total
        }), 200


    @app.get("/notes/<int:id>")
    @login_required
    def get_note(id):

        note = Note.query.get_or_404(id)

        if note.user_id != session["user_id"]:
            return jsonify({"error": "Unauthorized"}), 401

        return jsonify(note.to_dict()), 200


    @app.post("/notes")
    @login_required
    def create_note():

        data = request.get_json()

        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return jsonify({"error": "Title and content required"}), 400

        note = Note(
            title=title,
            content=content,
            user_id=session["user_id"]
        )

        db.session.add(note)
        db.session.commit()

        return jsonify(note.to_dict()), 201


    @app.patch("/notes/<int:id>")
    @login_required
    def update_note(id):

        note = Note.query.get_or_404(id)

        if note.user_id != session["user_id"]:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json()

        note.title = data.get("title", note.title)
        note.content = data.get("content", note.content)

        db.session.commit()

        return jsonify(note.to_dict()), 200


    @app.delete("/notes/<int:id>")
    @login_required
    def delete_note(id):

        note = Note.query.get_or_404(id)

        if note.user_id != session["user_id"]:
            return jsonify({"error": "Unauthorized"}), 401

        db.session.delete(note)
        db.session.commit()

        return {}, 204