from math import sqrt
def przeciwprostokatna(a,b=0):
    if b!=0:
        return sqrt(a**2+b**2)
    return a*sqrt(2)
print(przeciwprostokatna(2))
print(przeciwprostokatna(3,4))