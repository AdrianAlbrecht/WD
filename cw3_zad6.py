from math import sqrt
def promien_okregu(x,y,a=0,b=0):
    return sqrt((x-a)**2+(y-b)**2)
print(promien_okregu(7,4))
print(promien_okregu(2,2,1,1))