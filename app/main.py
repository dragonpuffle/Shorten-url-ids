from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(
    title='Shorten URL Ids',
    description='API service that shortens urls',
    lifespan=lifespan
)

app.include_router(router)
#uvicorn app.main:app --reload
