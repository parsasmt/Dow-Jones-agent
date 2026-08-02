from agent.intent import intent_detector
from agent.tool_selector import tool_selector
from agent.planner import planner
from agent.reasoner import reasoner


question = "Why did the Dow Jones fall today?"


intent = intent_detector.detect(question)

decision = tool_selector.select_tools(intent)

plan = planner.create_plan(question, decision)

result = reasoner.execute(plan)


for step in result.results:

    print("=" * 80)

    print("Step:", step.step_number)

    print("Tool:", step.tool.value)

    print("Success:", step.success)

    if step.success:

        print(step.data)

    else:

        print(step.error)