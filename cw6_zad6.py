import numpy as np

def wykresl():
    slowa=['michał','aamqpt','tordeh','ortcct','wprtib','ywoson']
    s=np.array([[x for x in slowa[i]] for i in range(6)])
    return s
        

print(wykresl())
