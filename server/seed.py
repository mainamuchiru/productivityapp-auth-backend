from .app import app
from .config import db
from .models import User, Note

with app.app_context():

    Note.query.delete()
    User.query.delete()

    john = User(username="john")
    john.set_password("password123")

    mary = User(username="mary")
    mary.set_password("password123")

    db.session.add_all([john, mary])
    db.session.commit()

    notes = [

        Note(
            title="Shopping List",
            content="Milk, Bread, Eggs",
            user_id=john.id
        ),

        Note(
            title="Homework",
            content="Finish Flask project",
            user_id=john.id
        ),

        Note(
            title="Workout",
            content="Gym at 6PM",
            user_id=mary.id
        ),

        Note(
            title="Books",
            content="Read Atomic Habits",
            user_id=mary.id
        )
    ]

    db.session.add_all(notes)
    db.session.commit()

    print("Database seeded.")