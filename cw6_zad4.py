import numpy as np

def generuj(m,n):
    return np.logspace(1,n,num=n,base=m)

print(generuj(2,10))