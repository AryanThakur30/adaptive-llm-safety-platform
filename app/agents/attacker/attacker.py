import random

from app.agents.attacker.strategies import ATTACK_STRATEGIES


class AttackerAgent:

    def attack(
        self,
        prompt: str
    ):

        strategy = random.choice(
            list(ATTACK_STRATEGIES.keys())
        )

        template = random.choice(
            ATTACK_STRATEGIES[strategy]
        )

        attacked_prompt = template.format(prompt)

        return {
            "strategy": strategy,
            "original_prompt": prompt,
            "attacked_prompt": attacked_prompt
        }


attacker = AttackerAgent()