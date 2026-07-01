import ollama
from app.config import settings


class TargetModel:
    def __init__(self):
        self.model = settings.OLLAMA_MODEL

    def generate(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]


target_model = TargetModel()