import random as rd

plik=open("z3.txt","w")
for i in range(20):
    li=rd.randint(1,100000)
    n=""
    for x in range(6-len(str(li))):
        n+='0'
    n=n+str(li)+'\n'
    plik.write(n)

plik.close