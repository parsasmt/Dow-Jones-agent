from database.db import SessionLocal
from database.models import User


db = SessionLocal()

try:

    users = db.query(User).all()

    print("=" * 80)
    print("ALL USERS")
    print("=" * 80)

    for user in users:

        print()
        print("Database ID:", user.id)
        print("User ID:", user.user_id)
        print("Created:", user.created_at)
        print("Conversations:", len(user.conversations))

        print("-" * 80)

finally:

    db.close()