s=input("enter the string:")
s1=s.replace(" ","").lower()
if s1==s1[::-1]:
	print("it is an palindrome")
else:
	print("it is not an palindeome")