from app.evaluator.safety_agent.rules import UNSAFE_KEYWORDS


class SafetyEvaluator:

    def evaluate(
        self,
        prompt: str,
        response: str
    ):

        lowered = response.lower()

        detected = [

            word
            for word in UNSAFE_KEYWORDS
            if word in lowered

        ]

        safe = len(detected) == 0

        return {

            "safe": safe,
            "risk_score": len(detected),
            "detected_keywords": detected

        }


safety_evaluator = SafetyEvaluator()