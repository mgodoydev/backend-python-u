from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Para iniciar el server uvicorn users:app --reload

#Entidad users
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id = 1, name="Mathias", surname="Godoy", url="https://mgodoydev.github.io/backend-python", age=22),
         User(id = 2, name="Cesar", surname="Molinas", url="cesar.com", age=22),
         User(id = 3, name="Mathias", surname="Molinas", url="tokeli.com", age=22)
         ]

@app.get("/usersjson")
async def usersjson():
    return [{"name" : "Mathias", "surname" : "Godoy", "url": "https://mgodoydev.github.io/backend-python/", "age": 22}]


@app.get("/users")
async def users():
    return users_list

#Path
@app.get("/user/{id}")
async def user(id: int):    
    return search_user(id)
 
 #Query   
@app.get("/user/")
async def user(id: int):    
    return search_user(id)


@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error": "El usuario ya existe"}
 
    users_list.append(user)
    return user
        

@app.put("/user/")
async def user(user: User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user  
            found = True
        
    if not found:
        return {"Error": "No se ha actualizado el usuario"}
        
    return user

@app.delete("/user/{id}")
async def user(id:int):
        found = False

        for index, saved_user in enumerate(users_list):
            if saved_user.id == id:
                del users_list[index]
                found = True
                return {"Exito": "El usuario se elimino correctamente"}
        
        if not found:
            return {"Error": "No se ha eliminado el usuario"}       
                
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list )
    try:
        return list(users)[0]
    except:
        return {"Error": "No se ha encontrado el usuario"}