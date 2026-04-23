import numpy as n

inter=n.array([89,70,56,77,66,93])
exter=n.array([58,90,89,78,55,69])
marks=inter+exter

print(f"internal marks:{inter}")
print(f"external marks:{exter}")
print(f"total marks:{marks}")

print(f"max:{n.max(marks)}\n")
print(f"min :{n.min(marks)}\n")
print(f"mean:{n.mean(marks)}\n")
print(f"sd:{n.std(marks)}")

print(inter*exter)