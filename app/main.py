from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)
#uvicorn app.main:app --reload
