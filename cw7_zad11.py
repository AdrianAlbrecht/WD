import numpy as np

a = np.arange(12)
b=a.reshape(3,4)
c=a.reshape(4,3)
d=a.reshape(2,6)
print(a)
print(b)
print(c)
print(d)
print("")
b=b.ravel()
c=c.ravel()
d=d.ravel()
print(a)
print(b)
print(c)
print(d)

#wyniki są identyczne