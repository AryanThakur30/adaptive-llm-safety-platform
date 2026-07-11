from fastapi import APIRouter

from app.agents.attacker.attacker import attacker

router = APIRouter()


@router.get("/attack")
def attack():

    result = attacker.attack(
        "Explain Kubernetes."
    )

    return result