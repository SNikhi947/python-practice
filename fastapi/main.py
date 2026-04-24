from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def h():
    return {
        "Hello": "This my first server creted by using fastapi"
    }

@app.get("/home")
def ho():
    return {"home":"hello wellcome!"}