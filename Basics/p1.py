name=input("enter ur name:")
age=int(input("enter ur age:"))
if age<18:
	print("you are young")
elif age<=60:
	print("you are in yourr prime")
elif age>=60:
	print("respect")
print(name,"!in 10 years you will be ",age+10,"years old!")