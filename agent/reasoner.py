from agent.schemas import (
    ExecutionPlan,
    ExecutionResult,
    StepResult,
    ToolType,
)

from tools.registry import tool_registry


class Reasoner:

    def execute(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionResult:

        results = []

        for step in plan.steps:

            if step.action == ToolType.NONE:

                continue

            tool = tool_registry.get(step.action)

            if tool is None:

                results.append(

                    StepResult(

                        step_number=step.step_number,

                        tool=step.action,

                        success=False,

                        error="Tool not found."

                    )

                )

                continue

            try:

                output = tool.run(plan.question)

                results.append(

                    StepResult(

                        step_number=step.step_number,

                        tool=step.action,

                        success=True,

                        output=output

                    )

                )

            except Exception as e:

                results.append(

                    StepResult(

                        step_number=step.step_number,

                        tool=step.action,

                        success=False,

                        error=str(e)

                    )

                )

        return ExecutionResult(

            results=results

        )


reasoner = Reasoner()