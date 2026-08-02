from tools.yahoo_tool import YahooTool



tool = YahooTool()


result = tool.run(
    "What is the current Dow Jones price?"
)



print("="*50)

print(result.tool)

print()

print(result.summary)

print()

print(result.raw_data)

print()

print(result.sources)