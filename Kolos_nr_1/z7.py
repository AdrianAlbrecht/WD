def lista(stri):
    li=stri.split(" ")
    nlen=0
    for s in li:
        temp=len(s)
        if(temp>nlen):
            nlen=temp
    nl=[]
    for x in li:
        nli=[]
        for y in x:
            nli+=str(y)
        for z in range(nlen-len(x)):
            nli+=['']
        nl+=[nli]
    print(nl)


stri='Ala ma kota'
s2='Cos tam 123456789'
print(stri,s2)
lista(stri)
lista(s2)