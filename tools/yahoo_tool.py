from agent.schemas import ToolOutput, ToolType

from tools.base_tool import BaseTool

from api.yahoo import yahoo_api



class YahooTool(BaseTool):


    name = "YAHOO_FINANCE"



    def run(self, question: str):


        data = yahoo_api.get_dow_jones()



        summary = f"""
Dow Jones Industrial Average:

Current Price:
{data.get("price")}

Open:
{data.get("open")}

High:
{data.get("high")}

Low:
{data.get("low")}

Volume:
{data.get("volume")}
"""


        return ToolOutput(

            tool=ToolType.YAHOO_FINANCE,

            summary=summary,

            raw_data=data,

            sources=[
                "Yahoo Finance"
            ]

        )