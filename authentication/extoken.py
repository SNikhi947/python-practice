from jose import JWTError,jwt
from datetime import datetime,timedelta

s_k="THIS-my-secrty-key"
algo="HS256"
exp=30

def tokengen(user: str) ->str:
    expire=datetime.utcnow()+timedelta(minutes=exp)
    payload={
        "sub":user,
        "exp":expire
    }
    T=jwt.encode(payload,s_k,algorithmyt=algo)
    return T

def tokenver(token : str) ->str:
    try:
        payload=jwt.decode(token,s_k,algorithms=[algo])
        username=payload.get("sub")
        if username == None:
            raise ValueError("Token has no subject")
        return username
    except JWTError:
        raise ValueError("Token as expired or no token valided")
    
token=tokengen("Nikhil")
print(f"token genterated:{token}")

ver=tokenver(token)
print(f"user is {ver}")