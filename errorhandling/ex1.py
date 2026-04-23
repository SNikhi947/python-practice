try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=a/b
    print(c)
except Exception as e:
    print(f"the error is{e}")
print("end of the exception program")