import json as j

json_t='{"name":"nikhil","age":19,"marks":[98,87,60]}'

dic=j.loads(json_t)
print(type(dic))
print(dic)
print(dic["name"])
print(dic["marks"])


nor={'name':'nikhil','age':20,'e-mail':'nikhil@gmail.com'}

json_s=j.dumps(nor,indent=4)

print(json_s)