import numpy as np

def fun(a,kierunek):
    czy=True
    if kierunek=="pion":
        if a.shape[1]%2==0:
            c=int(a.shape[1]/2)
            a1=a[:,:c]
            a2=a[:,c:]
        else:
            czy=False
    elif kierunek=="poziom":
        if a.shape[0]%2==0:
            c=int(a.shape[0]/2)
            a1=a[:c,:]
            a2=a[c:,:]
        else:
            czy=False
    else:
        print("Nieprawidlowe dane!")
    if czy==True:
        return a1,a2
    else:
        print("Wymiary tablicy nie pozwalaja na taki podzial")
        return 0,0

a=np.array([[ y for y in range(x*6+1,x*6+6+1)] for x in range(0,6)] )
print(a)
b1,b2=fun(a,"pion")
print(b1)
print(b2)
b1,b2=fun(a,"poziom")
print(b1)
print(b2)
a=np.array([[ y for y in range(x*5+1,x*5+5+1)] for x in range(0,5)] )
print(a)
b1,b2=fun(a,"pion")
print(b1)
print(b2)
b1,b2=fun(a,"poziom")
print(b1)
print(b2)
