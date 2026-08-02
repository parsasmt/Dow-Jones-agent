from database.db import SessionLocal
from database.crud import get_user, get_user_history


user_id = "Parsa123"

db = SessionLocal()

try:

    user = get_user(
        db,
        user_id
    )

    if user is None:

        print(
            f"User '{user_id}' does not exist."
        )

    else:

        print("=" * 80)
        print("USER INFORMATION")
        print("=" * 80)

        print(
            "Database ID:",
            user.id
        )

        print(
            "User ID:",
            user.user_id
        )

        print(
            "Created:",
            user.created_at
        )


        history = get_user_history(
            db,
            user_id
        )


        print()
        print("=" * 80)
        print("CONVERSATION HISTORY")
        print("=" * 80)


        if not history:

            print(
                "No conversations found."
            )

        else:

            for i, conversation in enumerate(
                history,
                start=1
            ):

                print()
                print(
                    f"Conversation #{i}"
                )

                print(
                    "Question:",
                    conversation.question
                )

                print(
                    "Answer:",
                    conversation.answer
                )

                print(
                    "Timestamp:",
                    conversation.timestamp
                )

                print("-" * 80)

finally:

    db.close()