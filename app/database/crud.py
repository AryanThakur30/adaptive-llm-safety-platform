from app.database.database import SessionLocal
from app.database.models import Experiment


print("🔥 CRUD MODULE LOADED")


def save_experiment(record: dict):

    print("🔥 SAVE_EXPERIMENT CALLED")

    db = SessionLocal()

    try:

        experiment = Experiment(
            experiment_id=record["experiment_id"],
            strategy=record["strategy"],
            original_prompt=record["original_prompt"],
            attacked_prompt=record["attacked_prompt"],
            response=record["response"],
            safe=record["safe"],
            risk_score=record["risk_score"],
            created_at=record["created_at"]
        )

        db.add(experiment)

        print("🔥 Object added to session")

        db.commit()

        print("✅ DATABASE COMMIT SUCCESS")

        db.refresh(experiment)

        print(f"✅ Database ID: {experiment.id}")

    except Exception as e:

        db.rollback()

        print("❌ DATABASE ERROR:")
        print(type(e).__name__)
        print(e)

        raise

    finally:

        db.close()

        print("🔒 Database session closed")


def get_all_experiments():

    db = SessionLocal()

    try:

        return db.query(Experiment).all()

    finally:

        db.close()


def get_experiment(experiment_id: str):

    db = SessionLocal()

    try:

        return (
            db.query(Experiment)
            .filter(
                Experiment.experiment_id == experiment_id
            )
            .first()
        )

    finally:

        db.close()


def get_statistics():

    db = SessionLocal()

    try:

        experiments = db.query(Experiment).all()

        total = len(experiments)

        safe = sum(
            1 for experiment in experiments
            if experiment.safe
        )

        unsafe = total - safe

        average_risk_score = (
            sum(
                experiment.risk_score
                for experiment in experiments
            ) / total
            if total > 0 else 0
        )

        strategies = {}

        for experiment in experiments:

            strategy = experiment.strategy

            strategies[strategy] = (
                strategies.get(strategy, 0) + 1
            )

        return {
            "total_experiments": total,
            "safe": safe,
            "unsafe": unsafe,
            "average_risk_score": round(
                average_risk_score,
                2
            ),
            "strategies": strategies
        }

    finally:

        db.close()


def search_experiments(keyword: str):

    db = SessionLocal()

    try:

        return (
            db.query(Experiment)
            .filter(
                Experiment.original_prompt.contains(keyword)
            )
            .all()
        )

    finally:

        db.close()


def filter_experiments(safe: bool):

    db = SessionLocal()

    try:

        return (
            db.query(Experiment)
            .filter(
                Experiment.safe == safe
            )
            .all()
        )

    finally:

        db.close()


def get_paginated_experiments(page: int, size: int):

    db = SessionLocal()

    try:

        total = db.query(Experiment).count()

        experiments = (
            db.query(Experiment)
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return {
            "page": page,
            "size": size,
            "total": total,
            "items": experiments
        }

    finally:

        db.close()


def delete_experiment(experiment_id: str):

    db = SessionLocal()

    try:

        experiment = (
            db.query(Experiment)
            .filter(
                Experiment.experiment_id == experiment_id
            )
            .first()
        )

        if experiment is None:
            return False

        db.delete(experiment)

        db.commit()

        return True

    finally:

        db.close()