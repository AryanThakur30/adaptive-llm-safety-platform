from fastapi import FastAPI
from pydantic import BaseModel

from app.core.config import settings
from app.services.llm_service import llm_service

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Adaptive LLM Safety Evaluation Platform",
    version="1.0.0"
)


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

    response = llm_service.generate(request.prompt)

    return {
        "prompt": request.prompt,
        "response": response
    }