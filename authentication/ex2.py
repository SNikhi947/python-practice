from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta

app=FastAPI()
f_p=CryptContext(schemes="bcrypt",deprecated="auto")
s_k="this-is -my-secrect-key"
algo="HS256"

db=[]
tk=[]

class userlogin(BaseModel):
    name:str
    password:str
class userverify(BaseModel):
    name:str
    password:str

class user(BaseModel):
    name:str

def tokengen(user:str) -> str:
    payload={
        "sub":user,
        "exp":datetime.utcnow()+timedelta(minutes=30)
    }
    return jwt.encode(payload,s_k,algorithm=algo)

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

@app.post("/token")
def tokencreate(us : user):
    for u in db:
        if u["name"]==us.name :
            tok=tokengen(us.name)
            new_t={
                "user":us.name,
                "token":tok
            }
            tk.append(new_t)
            return {"message":"creteated the token for the user"}
    raise HTTPException(status_code=404,detail="no user found")

@app.get("/tokdis")
def tokendis():
    return tk
    