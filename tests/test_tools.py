from tools.registry import tool_registry
from agent.schemas import ToolType


tools = [
    ToolType.RAG,
    ToolType.YAHOO_FINANCE,
    ToolType.TAVILY,
    ToolType.FRED
]


for tool_type in tools:

    tool = tool_registry.get(tool_type)

    print("=" * 50)

    print("Tool:", tool_type.value)

    result = tool.run(
        "Why did Dow Jones fall?"
    )

    print(result)