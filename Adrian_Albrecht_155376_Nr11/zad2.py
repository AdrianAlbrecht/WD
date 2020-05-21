import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19680822 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

kolory=['red','green','blue','yellow','violet','brown','cyan','orange']
markers=['.','o','v','1','s','P','X','$...$','d','*','8','p']


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100

xs = randrange(n, 0 , 100 )
ys = randrange(n, 0 , 100 )
for x in range(1,6,1):
    zs = randrange(n, 0+20*(x-1), 20*x+1)
    ax.scatter(xs, ys, zs, c =kolory[int(np.random.randint(0,len(kolory)))], marker =markers[int(np.random.randint(0,len(markers)))])

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()