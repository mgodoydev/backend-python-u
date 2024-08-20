#Para iniciar el server uvicorn main:app --reload

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastApi!"

@app.get("/url")
async def url():
    return {"url": "https://mgodoydev.github.io/backend-python/"}