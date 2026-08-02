from agent.schemas import ToolType

from tools.rag_tool import RagTool
from tools.yahoo_tool import YahooTool
from tools.tavily_tool import TavilyTool
from tools.fred_tool import FredTool


class ToolRegistry:

    def __init__(self):

        self.tools = {

            ToolType.RAG: RagTool(),

            ToolType.YAHOO_FINANCE: YahooTool(),

            ToolType.TAVILY: TavilyTool(),

            ToolType.FRED: FredTool(),

        }


    def get(self, tool_type):

        return self.tools.get(tool_type)



tool_registry = ToolRegistry()