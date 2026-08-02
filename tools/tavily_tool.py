from agent.schemas import (
    ToolOutput,
    ToolType
)

from tools.base_tool import BaseTool

from api.tavily import tavily_api



class TavilyTool(BaseTool):


    name = "TAVILY"



    def run(self, question: str):


        news = tavily_api.search_financial_news(
            question
        )


        summary = ""


        for item in news:

            summary += f"""

Title:
{item['title']}

Content:
{item['content']}

Source:
{item['url']}

---------------------

"""


        return ToolOutput(

            tool=ToolType.TAVILY,

            summary=summary,

            raw_data=news,

            sources=[
                item["url"]
                for item in news
            ]

        )