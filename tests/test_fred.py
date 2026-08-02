from tools.fred_tool import FredTool



tool = FredTool()


result = tool.run(
    "What is the current inflation rate?"
)



print(result.summary)

print(result.raw_data)