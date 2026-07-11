import json
from pathlib import Path


class RLHFDatasetGenerator:

    def __init__(self):

        self.output = Path("datasets/rlhf_dataset.jsonl")

        self.output.parent.mkdir(
            exist_ok=True
        )

    def save(self, record: dict):

        with open(
            self.output,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(record, default=str) + "\n"
            )


rlhf_generator = RLHFDatasetGenerator()