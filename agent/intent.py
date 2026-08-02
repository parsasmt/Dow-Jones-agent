import json

from agent.schemas import IntentResult, IntentType
from llm.llm import llm
from llm.output_parser import get_content
from llm.prompts import INTENT_PROMPT


class IntentDetector:

    def detect(self, question: str) -> IntentResult:

        messages = [
            {
                "role": "system",
                "content": INTENT_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]

        try:

            response = llm.chat(
                messages=messages,
                reasoning=True,
                temperature=0
            )

            content = get_content(response).strip()

            content = content.replace("```json", "")
            content = content.replace("```", "")
            content = content.strip()

            data = json.loads(content)

            return IntentResult(**data)

        except Exception as e:

            print(f"[IntentDetector] {e}")

            return IntentResult(
                intent=IntentType.UNKNOWN,
                confidence=0.0
            )


intent_detector = IntentDetector()