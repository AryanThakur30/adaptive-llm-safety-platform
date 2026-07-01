from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    DATABASE_URL = os.getenv("DATABASE_URL")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
    DEBUG = os.getenv("DEBUG") == "True"


settings = Settings()