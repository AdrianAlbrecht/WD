import numpy as np

b = np.array([[y*28 for y in range(x*3+1,x*3+3+1)] for x in range(0,3)])
a = np.arange(1,7).reshape(2,3)
print(a)
print(b)
for i in a.flat:
    print(i,end=" ")
    if i%3==0:
        print("")
for i in b.flat: #tu wywala error, że b.flat jest nieiterowalne pomimo iterowalnego typu, a sam kod sie wykonuje
    print(i,end=" ")
    if i%3==0:
        print("")