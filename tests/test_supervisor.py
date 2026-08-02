from agent.intent import intent_detector
from agent.tool_selector import tool_selector
from agent.planner import planner
from agent.reasoner import reasoner
from agent.supervisor import supervisor


question = "What is Dow Jones?"


intent = intent_detector.detect(question)

decision = tool_selector.select_tools(intent)

plan = planner.create_plan(question, decision)

execution = reasoner.execute(plan)

answer = supervisor.answer(

    question,

    execution

)

print(answer)