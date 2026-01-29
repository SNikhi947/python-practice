a=[10,20,30,50]
lent=len(a)
if lent%2==0:
	mid1=lent//2-1
	mid2=lent//2
	print(a[mid1],a[mid2])
else:
	mid=lent//2
	print(a[mid])