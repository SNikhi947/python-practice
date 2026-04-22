import requests as req

def safe_get(url):
    res=req.get(url)
    if res.status_code == 200:
        resd=res.json()
        print(res.status_code)
        print(resd)


url= "https://jsonplaceholder.typicode.com/users/1"

safe_get(url)