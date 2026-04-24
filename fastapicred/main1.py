from fastapi import FastAPI
from pydantic import BaseModel

st=[]
n_id=1

app=FastAPI()

class createst(BaseModel):
    name: str
    age: int
    city: str

@app.get("/")
def s():
    return {"hello":"welcome to server"}

@app.post("/students",status_code=201)
def addstu(s: createst):
    global n_id
    new_s={
        "id":n_id,
        "name":s.name,
        "age":s.age,
        "city":s.city
    }
    st.append(new_s)
    n_id+=1
    return new_s

@app.get("/students")
def get_students():
    return st