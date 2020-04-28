import numpy as np

tab=np.array([[y*30 for y in range(x*3+1,x*3+3+1)] for x in range(0,2)])
a=np.sin(tab)
tab2=np.random.rand(2,3)
b=np.cos(tab)
print(tab)
print(tab2)
print(a)
print(b)
print(a+b)
