import numpy as np

def tablica(n):
    return np.array([[ y for y in range(x*n+1,x*n+n+1)] for x in range(0,n)] )

print(tablica(6))