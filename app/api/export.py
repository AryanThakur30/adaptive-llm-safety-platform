from fastapi import APIRouter
from fastapi.responses import FileResponse

import csv
import json

from app.database.crud import get_all_experiments

router = APIRouter()


@router.get("/history/export/csv")
def export_csv():

    filename = "experiments.csv"

    experiments = get_all_experiments()

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Experiment ID",
            "Strategy",
            "Original Prompt",
            "Attacked Prompt",
            "Safe",
            "Risk Score",
            "Created At"
        ])

        for experiment in experiments:

            writer.writerow([
                experiment.experiment_id,
                experiment.strategy,
                experiment.original_prompt,
                experiment.attacked_prompt,
                experiment.safe,
                experiment.risk_score,
                experiment.created_at
            ])

    return FileResponse(
        filename,
        media_type="text/csv",
        filename=filename
    )


@router.get("/history/export/json")
def export_json():

    filename = "experiments.json"

    experiments = get_all_experiments()

    data = []

    for experiment in experiments:

        data.append({
            "experiment_id": experiment.experiment_id,
            "strategy": experiment.strategy,
            "original_prompt": experiment.original_prompt,
            "attacked_prompt": experiment.attacked_prompt,
            "response": experiment.response,
            "safe": experiment.safe,
            "risk_score": experiment.risk_score,
            "created_at": str(experiment.created_at)
        })

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return FileResponse(
        filename,
        media_type="application/json",
        filename=filename
    )