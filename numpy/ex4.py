import numpy as n

a=n.array([34,56,78,56,78,89,93,95])

print(f"marks:{a}")

print(a[a>70])
print(a[a%2==0])