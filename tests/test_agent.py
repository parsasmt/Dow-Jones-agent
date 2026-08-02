from database.db import init_db

from agent.orchestrator import agent

from agent.memory import (
    get_memory,
    format_memory
)

init_db()

user_id = "Ali123"


questions = [

    "What is the Dow Jones?",

    "When is a good time to invest in the Dow Jones?",

    "What is important news about the Dow Jones today?",

]



for question in questions:

    print()
    print("=" * 80)

    print(
        "USER ID:",
        user_id
    )

    print(
        "QUESTION:",
        question
    )

    print("=" * 80)


    try:

        response = agent.run(

            user_id=user_id,

            question=question

        )


        print()
        print("ANSWER:")
        print(response.answer)


        print()
        print("TOOLS USED:")

        for tool in response.tools_used:

            print(
                "-",
                tool.value
            )


    except Exception as e:

        print()
        print(
            "Agent Error:",
            e
        )



print()
print()
print("=" * 80)

print(
    "USER MEMORY"
)

print("=" * 80)


memory = get_memory(

    user_id=user_id,

    limit=10

)


if not memory:

    print(
        "No previous conversations."
    )

else:

    for index, item in enumerate(
        memory,
        start=1
    ):

        print()

        print(
            f"Conversation {index}"
        )

        print(
            "Question:",
            item["question"]
        )

        print(
            "Answer:",
            item["answer"]
        )

        print(
            "Timestamp:",
            item["timestamp"]
        )

        print(
            "-" * 60
        )



print()
print()
print("=" * 80)

print(
    "FORMATTED MEMORY"
)

print("=" * 80)


formatted_memory = format_memory(

    user_id=user_id,

    limit=10

)


print(
    formatted_memory
)