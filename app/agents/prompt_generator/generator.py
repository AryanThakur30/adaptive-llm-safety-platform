import random

from app.agents.prompt_generator.templates import PROMPT_TEMPLATES


class PromptGenerator:

    def generate(
        self,
        category: str,
        topic: str
    ):

        templates = PROMPT_TEMPLATES.get(category)

        if not templates:
            raise ValueError("Unknown category")

        template = random.choice(templates)

        return template.format(topic)


prompt_generator = PromptGenerator()