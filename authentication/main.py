from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

app=FastAPI()
f_p=CryptContext(schemes="bcrypt",deprecated="auto")

db=[]

class userlogin(BaseModel):
    name:str
    password:str
class userverify(BaseModel):
    name:str
    password:str

def hased(p: str) ->str:
    return f_p.hash(p)

def verify(v: str,h:str) ->bool:
    return f_p.verify(v,h)

@app.get("/")
def hi():
    return {"Hello":"welcome to server login"}

@app.post("/signup",status_code=201)
def usersignup(us :userlogin):
    for u in db:
        if u["name"]==us.name :
            return {"details":"the user name had been taken"}
    hashed_value=hased(us.password)
    new_value={
        "id":len(db)+1,
        "name":us.name,
        "password":hashed_value
    }
    db.append(new_value)
    return {"details":"the sign up is done u can go to /signin"}

@app.post("/signin")
def usersignin(us : userverify):
    user_name=None
    for u in db:
        if u["name"]==us.name :
            user_name=u
            break
    if not user_name:
        raise HTTPException(status_code=401,detail="Inivalid username or pasword")
    if verify(us.password,user_name["password"]):
        return {"user":"u have sussfully login to the server"}
    else:
        return {"user":"not allowed "}

@app.get("/user")
def userdetails():
    return db
