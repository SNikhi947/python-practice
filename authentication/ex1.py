from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

db=[]
id_x=1

class userrequest(BaseModel):
    name: str
    phno: int
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    phno: int

@app.get("/")
def hello():
    return {"message":"Hello wellcome back to the server"}

@app.post("/user",status_code=201,response_model=UserResponse)
def add(u :userrequest ):
    global id_x
    new_u={
        "id":id_x,
        "name":u.name,
        "phno":u.phno,
        "password":u.password
    }
    db.append(new_u)
    id_x+=1
    return new_u

@app.get("/user",response_model=List[UserResponse])
def get_users():
    return db

