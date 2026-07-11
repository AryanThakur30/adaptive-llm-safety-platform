from fastapi import FastAPI
from pydantic import BaseModel

from app.core.config import settings
from app.services.experiment_service import experiment_service

from app.api.test_prompt_generator import router as prompt_router
from app.api.test_attacker import router as attacker_router
from app.api.history import router as history_router
from app.api.export import router as export_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Adaptive LLM Safety Evaluation Platform",
    version="1.0.0"
)

app.include_router(prompt_router)
app.include_router(attacker_router)
app.include_router(history_router)
app.include_router(export_router)


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
async def home():
    return {
        "status": "running",
        "project": settings.PROJECT_NAME
    }


@app.post("/generate")
async def generate(request: PromptRequest):
    print("🔥 GENERATE API CALLED")
    return experiment_service.run(request.prompt)