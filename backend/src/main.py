from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api import api_router
from src.core.config import settings
from src.core.constants import API_PREFIX
from src.core.logger import logger, setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()

    logger.info("====================================")
    logger.info("Starting %s", settings.app_name)
    logger.info("Environment: %s", settings.app_env)
    logger.info("====================================")

    yield

    logger.info("Application shutdown complete")


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(
    api_router,
    prefix=API_PREFIX,
)


@app.get("/")
def root():
    return {
        "application": settings.app_name,
        "status": "running",
        "docs": "/docs",
    }