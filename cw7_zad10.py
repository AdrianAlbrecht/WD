import numpy as np

a=np.random.rand(9,9)
print(a)
b=a.reshape(3,27)
print(b)

#możliwości są takie, że ilość elelmentów po przeskalowaniu musi być taka sama jak przed czyli tutaj akurat 81