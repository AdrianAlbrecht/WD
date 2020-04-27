import numpy as np

def fun(n):
    return np.diag([x for x in range(n,0,-1)])

print(fun(6))