from database.db import SessionLocal
from database.crud import get_user_history


def get_memory(
    user_id: str,
    limit: int = 10
):
    """
    Retrieve the most recent conversations
    for a specific user.

    Parameters
    ----------
    user_id : str
        The user's unique ID.

    limit : int
        Maximum number of conversations to retrieve.

    Returns
    -------
    list
        List of previous conversations.
    """

    db = SessionLocal()

    try:

        history = get_user_history(
            db,
            user_id
        )

        # Keep only the latest N conversations
        history = history[-limit:]


        memory = []

        for item in history:

            memory.append({

                "question": item.question,

                "answer": item.answer,

                "timestamp": item.timestamp

            })


        return memory

    finally:

        db.close()


def format_memory(
    user_id: str,
    limit: int = 10
):
    """
    Convert conversation history into
    a text format that can later be
    passed to the LLM.
    """

    memory = get_memory(
        user_id=user_id,
        limit=limit
    )


    if not memory:

        return "No previous conversation history."


    formatted = []


    for item in memory:

        formatted.append(
            f"""
User:
{item["question"]}

Assistant:
{item["answer"]}

Time:
{item["timestamp"]}
"""
        )


    return "\n--------------------\n".join(
        formatted
    )