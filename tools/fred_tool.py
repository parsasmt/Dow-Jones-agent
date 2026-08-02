from agent.schemas import (
    ToolOutput,
    ToolType
)

from tools.base_tool import BaseTool

from api.fred import fred_api



class FredTool(BaseTool):


    name="FRED"



    def run(self, question: str):


        question_lower = question.lower()


        if "inflation" in question_lower:

            indicator = "CPI"


        elif "interest" in question_lower:

            indicator = "INTEREST_RATE"


        elif "unemployment" in question_lower:

            indicator="UNEMPLOYMENT"


        elif "gdp" in question_lower:

            indicator="GDP"


        else:

            indicator="CPI"



        data = fred_api.get_indicator(
            indicator
        )



        summary=f"""

Economic Indicator:

{indicator}


Current Value:

{data.get("value")}

"""


        return ToolOutput(

            tool=ToolType.FRED,

            summary=summary,

            raw_data=data,

            sources=[
                "Federal Reserve Economic Data"
            ]

        )