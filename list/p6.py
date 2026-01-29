a=[1,20,30,2,1]
b=a.copy()
lag1=max(b)
b.remove(lag1)
lag2=max(b)
print(lag2)