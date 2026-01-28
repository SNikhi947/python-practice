s=input("enter the string:")
lent=len(s)
print("length:",lent)

print("first character:",s[0])
print("last char:",s[-1])
if lent%2==0:
	mid1=lent//2-1
	mid2=lent//2
	print("middle:",s[mid1]+s[mid2])
else:
	mid=lent//2
	print("mid:",s[mid])