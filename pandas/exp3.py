import pandas as p

d=p.DataFrame({
    "name":["nikhil","ravi","naven","palani","sridhar","anil"],
    "age":[19,20,18,19,18,21],
    "cgpa":[9.7,7.8,8.4,7.6,8.7,9.0],
    "branch":["cse","ece","cse","ece","cse","cse"],
})

print(d)
print()
print(d.describe())
print()
print(d["cgpa"]>8.5)
print(max(d["cgpa"]))