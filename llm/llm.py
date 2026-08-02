import json
import requests

from config import config


class OpenRouterLLM:

    def __init__(self):

        self.url = f"{config.OPENROUTER_BASE_URL}/chat/completions"

        self.headers = {
            "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

    def chat(
        self,
        messages,
        reasoning=True,
        temperature=0.2,
    ):

        payload = {
            "model": config.MODEL_NAME,
            "messages": messages,
            "reasoning": {
                "enabled": reasoning
            },
            "temperature": temperature
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            data=json.dumps(payload),
            timeout=120
        )

        response.raise_for_status()

        return response.json()


llm = OpenRouterLLM()