import numpy as np

fib=[]
midfib=[]
a=1
b=1
for x in range(5):
    for y in range(5):
        temp=b
        b+=a
        a=temp
        midfib.append(a)
    fib.append(midfib)
    midfib=[]
an= np.array(fib)
print(an)

