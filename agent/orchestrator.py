from agent.intent import intent_detector
from agent.tool_selector import tool_selector
from agent.planner import planner
from agent.reasoner import reasoner
from agent.supervisor import supervisor
from database.db import (
    SessionLocal,
    init_db
)

from database.crud import (
    get_or_create_user,
    save_conversation
)
from agent.schemas import FinalAnswer



class DowJonesAgent:


    def run(
    self,
    user_id: str,
    question: str
    ):


        db = SessionLocal()

        try:

            # Make sure the user exists.
            user = get_or_create_user(
                db,
                user_id
            )

            print(
                f"User: {user.user_id}"
            )


            intent = intent_detector.detect(
                question
            )


            tool_decision = tool_selector.select_tools(
                intent
            )


            plan = planner.create_plan(
                question,
                tool_decision
            )


            execution = reasoner.execute(
                plan
            )

            answer = supervisor.answer(
                question,
                execution
            )


            save_conversation(

                db=db,

                user_id=user_id,

                question=question,

                answer=answer

            )


            return FinalAnswer(

                question=question,

                answer=answer,

                tools_used=[
                    result.tool
                    for result in execution.results
                ],

                success=True

            )

        finally:

            db.close()



agent = DowJonesAgent()