import pandas as pd

d={
    "name":["nikhil","palani","lokesh","rajesh"],
    "age":[19,20,20,21],
    "marks":[56,67,87,89]
}

df=pd.DataFrame(d)

print(df)
print(df.shape)
dd=df.to_csv()
with open("sample.csv","w") as f:
    f.write(dd)
print("updated the csv file")