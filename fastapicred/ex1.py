from fastapi import FastAPI
from pydantic import BaseModel

class player(BaseModel):
    name: str
    age: int
    team: str

pl=[
    {"id":1,"name":"nkr","age":28,"team":"srh"},
    {"id":2,"name":"abhi","age":24,"team":"srh"},
    {"id":3,"name":"rohit","age":38,"team":"mi"}
]

app=FastAPI()

@app.get("/")
def hello():
    return {"hello":"every one wellcome to my server"}

@app.get("/players")
def display():
    return pl

@app.put("/players/{p_id}")
def update(p_id : int,p: player):
    for i,s in enumerate(pl):
        if s["id"] == p_id :
            pl[i]={
                "id":p_id,
                "name":p.name,
                "age":p.age,
                "team":p.team
            }
            return pl[i]
        
    return {"error":"no player is found"}

@app.delete("/players/{p_id}")
def delete_player(p_id : int):
    for i,s in enumerate(pl):
        if s["id"] == p_id:
            pl.pop(i)
            return {"player":"deleteded for the list"}
    return {"error":"404 player not found"}

