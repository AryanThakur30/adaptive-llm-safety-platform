from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class Experiment:

    experiment_id: str
    prompt: str
    model: str
    status: str
    created_at: datetime

    @classmethod
    def create(cls, prompt: str, model: str):

        return cls(
            experiment_id=str(uuid4()),
            prompt=prompt,
            model=model,
            status="running",
            created_at=datetime.utcnow()
        )