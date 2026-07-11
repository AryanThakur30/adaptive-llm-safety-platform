print("🔥 EXPERIMENT SERVICE LOADED")

import time
from datetime import datetime

from app.models.experiment import Experiment
from app.services.llm_service import llm_service
from app.agents.attacker.attacker import attacker
from app.evaluator.safety_agent.evaluator import safety_evaluator
from app.dataset.rlhf.generator import rlhf_generator
from app.database.crud import save_experiment


class ExperimentService:

    def run(self, prompt: str):

        print("🔥 RUN METHOD CALLED")

        experiment = Experiment.create(
            prompt=prompt,
            model=llm_service.model
        )

        attack = attacker.attack(prompt)

        start = time.perf_counter()

        response = llm_service.generate(
            attack["attacked_prompt"]
        )

        execution_time = round(
            (time.perf_counter() - start) * 1000,
            2
        )

        evaluation = safety_evaluator.evaluate(
            attack["attacked_prompt"],
            response
        )

        experiment.status = "completed"

        created_at = datetime.utcnow()

        # Database Record
        record = {
            "experiment_id": experiment.experiment_id,
            "strategy": attack["strategy"],
            "original_prompt": attack["original_prompt"],
            "attacked_prompt": attack["attacked_prompt"],
            "response": response,
            "safe": evaluation["safe"],
            "risk_score": evaluation["risk_score"],
            "detected_keywords": evaluation["detected_keywords"],
            "created_at": created_at
        }

        # RLHF Record (JSON Serializable)
        rlhf_record = record.copy()
        rlhf_record["created_at"] = created_at.isoformat()

        print("🔥 Saving RLHF dataset...")
        rlhf_generator.save(rlhf_record)

        print("🔥 Saving to database...")
        save_experiment(record)

        print("✅ Experiment completed successfully")

        return {
            "experiment_id": experiment.experiment_id,
            "model": experiment.model,
            "status": experiment.status,
            "strategy": attack["strategy"],
            "original_prompt": attack["original_prompt"],
            "attacked_prompt": attack["attacked_prompt"],
            "execution_time_ms": execution_time,
            "response": response,
            "safe": evaluation["safe"],
            "risk_score": evaluation["risk_score"],
            "detected_keywords": evaluation["detected_keywords"]
        }


experiment_service = ExperimentService()