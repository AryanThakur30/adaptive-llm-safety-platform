import time

from app.models.experiment import Experiment
from app.services.llm_service import llm_service


class ExperimentService:

    def run(self, prompt: str):

        experiment = Experiment.create(
            prompt=prompt,
            model=llm_service.model
        )

        start = time.perf_counter()

        response = llm_service.generate(prompt)

        execution_time = round(
            (time.perf_counter() - start) * 1000,
            2
        )

        experiment.status = "completed"

        return {
            "experiment_id": experiment.experiment_id,
            "model": experiment.model,
            "status": experiment.status,
            "execution_time_ms": execution_time,
            "prompt": prompt,
            "response": response
        }


experiment_service = ExperimentService()