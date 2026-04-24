from fastapi import FastAPI
from pydantic import BaseModel

class create(BaseModel):
    name: str
    age: int

app=FastAPI()
global n_id
st=[
    {"id":1,"name":"Nikhil","age":20},
    {"id":2,"name":"naveen","age":21},
    {"id":3,"name":"ravi","age":23}
]

@app.get("/")
def h():
    return {"Hello Everyone":"Wellcome to the my server"}

@app.get("/students")
def s():
    return st 

@app.get("/students/{st_id}")
def id(st_id : int):
    for stu in st:
        if stu["id"] == st_id:
            return stu
    return {"Error":"Not found 404"}

@app.post("/students",status_code=201)
def new(n_s : create):
    n_id = st[-1]["id"]+1 if st else 1
    new= {
        "id":n_id,
        "name":n_s.name,
        "age":n_s.age
    }
    st.append(new)
    n_id +=1
    return new

@app.delete("/students/{st_id}")
def de(st_id : int):
    for i,s in enumerate(st):
        if s["id"]== st_id:
            st.pop(i)
            return {"student":"deleted for the list"}
    return {"student":"not found with the id"}

@app.put("/students/{s_id}")
def up(s_id : int,st_u : create):
    for i,s in enumerate(st):
        if s["id"] == s_id:
            st[i]={
                "id":s_id,
                "name":st_u.name,
                "age":st_u.age
            }
            return st[i]
    return {"student":"not Found 404"}
