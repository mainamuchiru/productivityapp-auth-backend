from server import app
from server.config import db
from server.models import User, Note

with app.app_context():
    # Clear existing data
    Note.query.delete()
    User.query.delete()

    # Create a user
    user = User(username="john")
    user.set_password("password123")

    # Create notes
    note1 = Note(
        title="Shopping List",
        content="Milk, Eggs, Bread",
        user=user
    )

    note2 = Note(
        title="Homework",
        content="Finish Flask assignment",
        user=user
    )

    note3 = Note(
        title="Reminder",
        content="Call Mom at 7 PM",
        user=user
    )

    # Save to database
    db.session.add(user)
    db.session.add_all([note1, note2, note3])
    db.session.commit()

    print("🌱 Database seeded successfully!")