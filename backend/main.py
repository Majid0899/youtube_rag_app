from fastapi import FastAPI
from backend.api.routes import router
from backend.core.logging import setup_logger

setup_logger()

app = FastAPI(title="YouTube RAG API")

app.include_router(router)
