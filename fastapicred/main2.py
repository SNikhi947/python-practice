from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class create(BaseModel):
    name: str
    age: int
    team: str

app=FastAPI()
global n_id
st=[
    {"id":1,"name":"Abhi","age":24,"team":"srh"},
    {"id":2,"name":"axer","age":21,"team":"dc"},
    {"id":3,"name":"pat cummins","age":23,"team":"srh"}
]

@app.get("/")
def h():
    return {"Hello Everyone":"Wellcome to the my server to see the players details"}

@app.get("/players")
def s():
    return st 

@app.get("/players/search")
def get_player(team:Optional[str]=None,limit:int=10):
    res=st
    if team:
        res=[s for s in res if s["team"]==team]
    return res[:limit]

@app.get("/players/{st_id}")
def id(st_id : int):
    for stu in st:
        if stu["id"] == st_id:
            return stu
    return {"Error":"Not found 404"}

@app.post("/players",status_code=201)
def new(n_s : create):
    n_id = st[-1]["id"]+1 if st else 1
    new= {
        "id":n_id,
        "name":n_s.name,
        "age":n_s.age,
        "team":n_s.team
    }
    st.append(new)
    n_id +=1
    return new

@app.delete("/players/{st_id}")
def de(st_id : int):
    for i,s in enumerate(st):
        if s["id"]== st_id:
            st.pop(i)
            return {"student":"deleted for the list"}
    return {"student":"not found with the id"}

@app.put("/players/{s_id}")
def up(s_id : int,st_u : create):
    for i,s in enumerate(st):
        if s["id"] == s_id:
            st[i]={
                "id":s_id,
                "name":st_u.name,
                "age":st_u.age,
                "team":st_u.team
            }
            return st[i]
    return {"student":"not Found 404"}

