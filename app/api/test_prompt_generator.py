from fastapi import APIRouter

from app.agents.prompt_generator.generator import prompt_generator

router = APIRouter()


@router.get("/prompt")
def generate_prompt():

    prompt = prompt_generator.generate(
        category="programming",
        topic="Kubernetes"
    )

    return {
        "generated_prompt": prompt
    }