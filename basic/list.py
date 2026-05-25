l=[90,43,32,50,10,30,40,60]
count=0
sum=0
for i in l:
    sum+=i
    count=count+1
print(count)
print(sum)
print(max(l))
print(min(l))
li=sorted(l)
print("second largest number:",li[-2])
l2=[56,78,90,60]
print(l+l2)