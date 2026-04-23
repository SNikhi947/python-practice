import numpy as n

arr=n.array( [45, 78, 92, 33, 55, 88, 61, 40])
print(f"total:{n.sum(arr)}")
print(f"max:{n.max(arr)}")
print(f"min:{n.min(arr)}")
print(f"mean{n.mean(arr)}")
print(f"mean{n.std(arr)}")

print(len(arr[arr>60]))

print(arr[arr>50])
print(arr+5)