from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional, Any



class IntentType(str, Enum):
    GENERAL_KNOWLEDGE = "GENERAL_KNOWLEDGE"
    COMPANY_INFORMATION = "COMPANY_INFORMATION"
    MARKET_NEWS = "MARKET_NEWS"
    LIVE_MARKET_DATA = "LIVE_MARKET_DATA"
    ECONOMIC_INDICATOR = "ECONOMIC_INDICATOR"
    HISTORICAL_EVENT = "HISTORICAL_EVENT"
    COMPARISON = "COMPARISON"
    ANALYSIS = "ANALYSIS"
    UNKNOWN = "UNKNOWN"


class IntentResult(BaseModel):
    intent: IntentType
    confidence: float = Field(ge=0.0, le=1.0)



class ToolType(str, Enum):
    RAG = "RAG"
    YAHOO_FINANCE = "YAHOO_FINANCE"
    TAVILY = "TAVILY"
    FRED = "FRED"
    NONE = "NONE"


class ToolDecision(BaseModel):
    tools: List[ToolType]
    reason: str



class PlanStep(BaseModel):

    step_number: int

    action: ToolType

    description: str


class ExecutionPlan(BaseModel):

    steps: List[PlanStep]

    question: str

    total_steps: int



class StepResult(BaseModel):

    step_number: int

    tool: ToolType

    success: bool

    data: Any = None

    error: Optional[str] = None



class ToolOutput(BaseModel):
    """
    Standard output format for every tool.
    """

    tool: ToolType

    summary: str

    raw_data: Any = None

    sources: List[str] = []


class StepResult(BaseModel):

    step_number: int

    tool: ToolType

    success: bool

    output: Optional[ToolOutput] = None

    error: Optional[str] = None


class ExecutionResult(BaseModel):

    results: List[StepResult]
    

class FinalAnswer(BaseModel):

    question: str

    answer: str

    tools_used: list[ToolType]

    success: bool