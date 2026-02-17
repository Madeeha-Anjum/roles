from app.core.loggers import setup_logging; setup_logging(); # fmt: skip
from app.core.settings import settings
from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)
logger.debug(
    f"""
        PROJECT_NAME: {settings.PROJECT_NAME}
        ENVIRONMENT: {settings.ENVIRONMENT} 
        DEBUG: {settings.DEBUG}
        DATABASE_URL: {settings.DIRECT_DATABASE_URL}
    """,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    #  BEFORE the app starts receiving requests
    logger.debug("⭐ ⭐ ⭐ Starting up ⭐ ⭐ ⭐ \n")

    yield
    # AFTER the app finishes (shutdown)
    # you normally close DB pools, cleanup stuff here
    logger.debug("⭐ ⭐ ⭐ Shutting down⭐ ⭐ ⭐ \n")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {
        "message": "Hello World",
    }
