a=[10,40,30,50]
first=0
last=len(a)-1
c=a[last]
a[last]=a[first]
a[first]=c
print(a)

