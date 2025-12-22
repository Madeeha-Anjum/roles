from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ⭐ This runs BEFORE the app starts receiving requests
    print("Starting up...")

    yield

    # ⭐ This runs AFTER the app finishes (shutdown)
    # you normally close DB pools, cleanup stuff here
    print("Shutting down...")
    pass


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "DATABASE_URL": settings.DIRECT_DATABASE_URL,
        "ENVIRONMENT": settings.ENVIRONMENT,
        "DEBUG": settings.DEBUG,
        "PROJECT_NAME": settings.PROJECT_NAßME,
    }
