import numpy as np

a=np.random.rand(3,3)
b=np.random.rand(4,4)
print(a)
print(b)
print(a.min(axis=0))
print(a.min(axis=1))
print(b.min(axis=0))
print(b.min(axis=1))