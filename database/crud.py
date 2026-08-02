from sqlalchemy.orm import Session

from database.models import (
    User,
    Conversation
)

def get_user(
    db: Session,
    user_id: str
):

    return (
        db.query(User)
        .filter(
            User.user_id == user_id
        )
        .first()
    )

def create_user(
    db: Session,
    user_id: str
):

    user = User(
        user_id=user_id
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

def get_or_create_user(
    db: Session,
    user_id: str
):

    user = get_user(
        db,
        user_id
    )

    if user is None:

        user = create_user(
            db,
            user_id
        )

    return user

def save_conversation(
    db: Session,
    user_id: str,
    question: str,
    answer: str
):

    user = get_or_create_user(
        db,
        user_id
    )

    conversation = Conversation(

        user_id=user.id,

        question=question,

        answer=answer

    )

    db.add(conversation)

    db.commit()

    db.refresh(conversation)

    return conversation


def get_user_history(
    db: Session,
    user_id: str
):

    user = get_user(
        db,
        user_id
    )

    if user is None:

        return []


    return (
        db.query(Conversation)

        .filter(
            Conversation.user_id == user.id
        )

        .order_by(
            Conversation.timestamp.asc()
        )

        .all()
    )