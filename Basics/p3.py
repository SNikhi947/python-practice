a=int(input("enter the no:"))
nat=("odd","even")[a%2==0]
if a%5==0:
	print(nat,"& div by 5")
else:
	print(nat)
 