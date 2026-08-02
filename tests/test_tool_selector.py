from agent.intent import intent_detector
from agent.tool_selector import tool_selector


questions = [

    "What is the Dow Jones?",

    "What is today's Dow Jones price?",

    "Why did Apple stock rise today?",

    "Compare the Dow Jones and Nasdaq.",

    "What is CPI?",

    "Tell me about the 2008 financial crisis."

]


if __name__ == "__main__":

    for question in questions:

        print("=" * 80)

        print("Question:")
        print(question)

        print()

        intent = intent_detector.detect(question)

        print("Intent:")
        print(intent.intent.value)

        print()

        decision = tool_selector.select_tools(intent)

        print("Selected Tools:")

        for tool in decision.tools:
            print(f"- {tool.value}")

        print()

        print("Reason:")
        print(decision.reason)

        print()