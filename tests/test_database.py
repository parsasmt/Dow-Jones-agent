from database.db import (
    init_db,
    SessionLocal
)

from database.crud import (
    get_user,
    get_or_create_user,
    save_conversation,
    get_user_history
)

init_db()


db = SessionLocal()


try:

    user_id = "Parsa123"


    user = get_user(
        db,
        user_id
    )


    if user is None:

        print(
            f"User '{user_id}' does not exist."
        )

        user = get_or_create_user(
            db,
            user_id
        )

        print(
            f"Created user '{user_id}'."
        )

    else:

        print(
            f"User '{user_id}' already exists."
        )


    conversation = save_conversation(

        db=db,

        user_id=user_id,

        question="What is the Dow Jones?",

        answer=(
            "The Dow Jones Industrial Average "
            "is a price-weighted stock market index."
        )

    )


    print()
    print(
        "Saved conversation ID:",
        conversation.id
    )


    history = get_user_history(
        db,
        user_id
    )


    print()
    print("=" * 70)
    print("USER HISTORY")
    print("=" * 70)


    for item in history:

        print()

        print(
            "Conversation ID:",
            item.id
        )

        print(
            "Question:",
            item.question
        )

        print(
            "Answer:",
            item.answer
        )

        print(
            "Timestamp:",
            item.timestamp
        )

        print("-" * 70)


finally:

    db.close()