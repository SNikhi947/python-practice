import pandas as p

csv_t="""name,rollno,mat,phy,che
nikhil,m597,90,87,67
naveen,m586,68,56,78
ravi,m567,89,78,87
sai,m564,87,84,93
"""

with open("st.csv","w") as f:
    f.write(csv_t)

print("enter the details in csv")

d=p.read_csv("st.csv")

print(f"{d}\n")

print(d.describe())

print(d.head(5))
print()
print(d.tail(3))