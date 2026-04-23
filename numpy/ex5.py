import numpy as n

m=n.array([
    [89,90,60],
    [56,98,70],
    [90,98,89]
    ])

print(m.shape)
print(m[0])
print(m[0][2])

print(m[m>60])
print(m[:,0])
print(m[0,:])