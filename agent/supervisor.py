from llm.llm import llm
from llm.output_parser import get_content
from llm.prompts import SUPERVISOR_PROMPT

from agent.schemas import ExecutionResult


class Supervisor:

    def _build_context(
        self,
        execution: ExecutionResult
    ) -> str:

        context = ""

        for result in execution.results:

            if not result.success:

                continue

            context += (
                f"\n"
                f"=============================\n"
                f"{result.tool.value}\n"
                f"=============================\n"
                f"{result.output.summary}\n"
            )

        return context

    def answer(
        self,
        question: str,
        execution: ExecutionResult
    ) -> str:

        context = self._build_context(execution)

        messages = [

            {
                "role":"system",
                "content":
                SUPERVISOR_PROMPT
            },

            {
                "role":"user",
                "content":
                f"""
Question:

{question}

Collected Information:

{context}

Write the best possible answer.
"""
            }

        ]

        response = llm.chat(

            messages,

            reasoning=True,

            temperature=0.2

        )

        return get_content(response)


supervisor = Supervisor()