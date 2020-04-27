import numpy as np

def wykresl():
    slowa=['michał','aamqpt','pordeh','mrtcct','pdrtib','ywoson']
    s=np.array([[x for x in slowa[i]] for i in range(6)])
    return s
        

print(wykresl())