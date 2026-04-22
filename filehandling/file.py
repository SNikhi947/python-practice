with open("sample.txt","w") as f:
	f.write("Nikhil \n")
	f.write("navven\n")
	f.write("ravi\n")
print("entered the details in the file")

with open("sample.txt","r") as f:
	c=f.read()
print(f"the content {c}")