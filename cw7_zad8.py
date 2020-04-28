import numpy as np

a=np.array([[y*28 for y in range(x*3+1,x*3+3+1)] for x in range(0,3)])
print(a)
for j in range(0,a.shape[0]):
    for i in range(0,a.shape[1]):
        print(a[i,j], end=" ")
    print("")