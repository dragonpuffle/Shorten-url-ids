from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def start():
    return {'Ok': 'Success'}

#uvicorn app.main:app --reload