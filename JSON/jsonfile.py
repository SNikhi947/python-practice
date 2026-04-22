import json as j

nor={'name':'nikhil','age':20,'e-mail':'nikhil@gmail.com'}

with open("sample.json","w") as f:
    j.dump(nor,f,indent=4)
print("JSON formate entered in the file")

with open("sample.json","r") as f:
    a=j.load(f)
print(a["name"])