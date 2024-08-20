from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Para iniciar el server uvicorn users:app --reload

#Entidad users
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(name="Mathias", surname="Godoy", url="https://mgodoydev.github.io/backend-python", age=22),
         User(name="Cesar", surname="Molinas", url="cesar.com", age=22),
         User(name="Mathias", surname="Molinas", url="tokeli.com", age=22)
         ]

@app.get("/usersjson")
async def usersjson():
    return [{"name" : "Mathias", "surname" : "Godoy", "url": "https://mgodoydev.github.io/backend-python/", "age": 22}]

@app.get("/users")
async def users():
    return users_list