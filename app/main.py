from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title='Shorten URL Ids',
    description='API service that shortens urls',
)
app.include_router(router)
#uvicorn app.main:app --reload
