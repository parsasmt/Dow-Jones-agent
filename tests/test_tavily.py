from tools.tavily_tool import TavilyTool



tool = TavilyTool()


result = tool.run(
    "Why did Dow Jones fall today?"
)



print("="*50)

print(result.tool)

print()

print(result.summary)

print()

print(result.sources)