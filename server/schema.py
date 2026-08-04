from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import User, Note


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("_password_hash",)


class NoteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        include_fk = True


# Single objects
user_schema = UserSchema()
note_schema = NoteSchema()

# Multiple objects
users_schema = UserSchema(many=True)
notes_schema = NoteSchema(many=True)