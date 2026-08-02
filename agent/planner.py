from agent.schemas import (
    ExecutionPlan,
    PlanStep,
    ToolDecision,
    ToolType,
)


class Planner:

    """
    Creates an execution plan based on the selected tools.
    """

    def create_plan(
        self,
        question: str,
        tool_decision: ToolDecision,
    ) -> ExecutionPlan:

        steps = []

        step_number = 1

        for tool in tool_decision.tools:

            if tool == ToolType.RAG:

                steps.append(
                    PlanStep(
                        step_number=step_number,
                        action=ToolType.RAG,
                        description="Retrieve relevant information from the knowledge base."
                    )
                )

                step_number += 1

            elif tool == ToolType.YAHOO_FINANCE:

                steps.append(
                    PlanStep(
                        step_number=step_number,
                        action=ToolType.YAHOO_FINANCE,
                        description="Retrieve live market data from Yahoo Finance."
                    )
                )

                step_number += 1

            elif tool == ToolType.TAVILY:

                steps.append(
                    PlanStep(
                        step_number=step_number,
                        action=ToolType.TAVILY,
                        description="Retrieve recent financial news."
                    )
                )

                step_number += 1

            elif tool == ToolType.FRED:

                steps.append(
                    PlanStep(
                        step_number=step_number,
                        action=ToolType.FRED,
                        description="Retrieve official economic indicators."
                    )
                )

                step_number += 1

        steps.append(
            PlanStep(
                step_number=step_number,
                action=ToolType.NONE,
                description="Generate the final answer using all collected information."
            )
        )

        return ExecutionPlan(
            question=question,
            steps=steps,
            total_steps=len(steps),
        )


planner = Planner()