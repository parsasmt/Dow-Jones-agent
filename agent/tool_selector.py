from agent.schemas import (
    IntentType,
    IntentResult,
    ToolDecision,
    ToolType,
)


class ToolSelector:
    """
    Selects which tools should be used based on
    the detected intent.
    """

    def __init__(self):

        self.intent_to_tools = {

            IntentType.GENERAL_KNOWLEDGE: (
                [ToolType.RAG],
                "General knowledge questions are answered from the knowledge base."
            ),

            IntentType.COMPANY_INFORMATION: (
                [ToolType.RAG],
                "Company information is retrieved from the knowledge base."
            ),

            IntentType.MARKET_NEWS: (
                [ToolType.RAG, ToolType.TAVILY],
                "Use RAG for background knowledge and Tavily for the latest news."
            ),

            IntentType.LIVE_MARKET_DATA: (
                [ToolType.YAHOO_FINANCE],
                "Live prices are retrieved from Yahoo Finance."
            ),

            IntentType.ECONOMIC_INDICATOR: (
                [ToolType.RAG, ToolType.FRED],
                "Use RAG for explanations and FRED for official economic data."
            ),

            IntentType.HISTORICAL_EVENT: (
                [ToolType.RAG],
                "Historical events are stored in the knowledge base."
            ),

            IntentType.COMPARISON: (
                [ToolType.RAG, ToolType.YAHOO_FINANCE],
                "Comparison requires background knowledge and live market data."
            ),

            IntentType.ANALYSIS: (
                [ToolType.RAG, ToolType.YAHOO_FINANCE, ToolType.TAVILY],
                "Analysis combines knowledge, live prices, and recent news."
            ),

            IntentType.UNKNOWN: (
                [ToolType.NONE],
                "Unable to determine the appropriate tools."
            ),
        }

    def select_tools(
        self,
        intent_result: IntentResult
    ) -> ToolDecision:

        tools, reason = self.intent_to_tools.get(
            intent_result.intent,
            (
                [ToolType.NONE],
                "Unknown intent."
            )
        )

        return ToolDecision(
            tools=tools,
            reason=reason
        )


tool_selector = ToolSelector()