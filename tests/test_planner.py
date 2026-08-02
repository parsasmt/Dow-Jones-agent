from agent.intent import intent_detector
from agent.tool_selector import tool_selector
from agent.planner import planner


questions = [

    "What is Dow Jones?",

    "Why did Apple stock rise today?",

    "What is today's Dow Jones price?",

    "What is CPI?",

    "Compare Dow Jones and Nasdaq."

]


if __name__ == "__main__":

    for question in questions:

        print("=" * 80)

        print("QUESTION")

        print(question)

        print()

        intent = intent_detector.detect(question)

        print("INTENT")

        print(intent.intent.value)

        print()

        decision = tool_selector.select_tools(intent)

        print("TOOLS")

        for tool in decision.tools:

            print("-", tool.value)

        print()

        plan = planner.create_plan(
            question,
            decision
        )

        print("EXECUTION PLAN")

        for step in plan.steps:

            print(
                f"{step.step_number}. "
                f"[{step.action.value}] "
                f"{step.description}"
            )

        print()