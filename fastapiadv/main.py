from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

class student(BaseModel):
    name:str=Field(min_length=2,max_length=50)
    age:int=Field(gt=1,lt=100)
    email:str=Field(min_length=1,max_length=60)
    phno:Optional[str]=Field(default="None")
    city:str=Field(default="unknow",max_length=120)

app=FastAPI()

st=[]

@app.get("/")
def hello():
    return {"hello everyone":"wellcome to my server"}

@app.get("/stud")
def display():
    return st

@app.post("/stud",status_code=201)
def adding(s : student):
    new={
        "name":s.name,
        "age":s.age,
        "email":s.email,
        "phno":s.phno,
        "city":s.city
    }
    st.append(new)
    return new
