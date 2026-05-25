import math
a,b=10,20
print("sum:",a+b)
ce=30
print("Celsius to Fahrenheit:",(ce*(9/5))+32)
print(a,b)
a,b=b,a
print(a,b)
p,t,r=1000,2,5
print("simple interest:",(p*t*r)/100)
rd=4
print("area of circle:",math.pi*rd*rd)
num=str(103475488367)
count=0
for i in num:
    count=count+1
print(count)
op=input("enter the opration:")
match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _:
        print("*******error*******")