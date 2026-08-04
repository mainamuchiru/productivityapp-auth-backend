from .app import app
from .config import db
from .models import User, Note

with app.app_context():

    db.drop_all()
    db.create_all()

    john = User(username="john")
    john.set_password("password123")

    mary = User(username="mary")
    mary.set_password("password123")

    db.session.add_all([john, mary])
    db.session.commit()

    notes = [
        Note(
            title="Shopping List",
            content="Milk, Bread",
            user_id=john.id
        ),
        Note(
            title="Homework",
            content="Finish Flask project",
            user_id=john.id
        ),
        Note(
            title="Workout",
            content="Leg day",
            user_id=mary.id
        ),
        Note(
            title="Books",
            content="Atomic Habits",
            user_id=mary.id
        )
    ]

    db.session.add_all(notes)
    db.session.commit()

    print("Database seeded successfully.")