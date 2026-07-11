from fastapi import APIRouter, HTTPException

from app.database.crud import (
    get_all_experiments,
    get_experiment,
    get_statistics,
    search_experiments,
    filter_experiments,
    get_paginated_experiments,
    delete_experiment
)

router = APIRouter()


@router.get("/history")
def history():

    return get_all_experiments()


@router.get("/history/search")
def search(keyword: str):

    return search_experiments(keyword)


@router.get("/history/filter")
def filter_history(safe: bool):

    return filter_experiments(safe)


@router.get("/history/page")
def pagination(page: int = 1, size: int = 10):

    return get_paginated_experiments(page, size)


@router.get("/history/{experiment_id}")
def history_detail(experiment_id: str):

    experiment = get_experiment(experiment_id)

    if experiment is None:
        raise HTTPException(
            status_code=404,
            detail="Experiment not found"
        )

    return experiment


@router.delete("/history/{experiment_id}")
def delete_history(experiment_id: str):

    deleted = delete_experiment(experiment_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Experiment not found"
        )

    return {
        "message": "Experiment deleted successfully"
    }


@router.get("/stats")
def statistics():

    return get_statistics()