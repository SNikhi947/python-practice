from fastapi import FastAPI

app=FastAPI()

st=[
    {"id":1,"name":"nikhil","age":19},
    {"id":2,"name":"lokesh","age":21},
    {"id":3,"name":"palian","age":22},
    {"id":4,"name":"pr rajesh","age":56}
]

@app.get("/")
def hello():
    return {"Hello":"hi evry good to see u"}

@app.get("/students")
def stu():
    return st

@app.get("/students/count")
def count():
    return {"total":len(st)}

@app.get("/students/{stu_id}")
def details(stu_id : int):
    for s in st:
        if s["id"]== stu_id :
            return s
    else:
        return {"details":"not found 404"}
