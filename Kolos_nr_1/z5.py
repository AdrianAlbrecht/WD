def srodek(lisa):
    lisa.sort()
    if(len(lisa)%2==0):
        return (lisa[int(len(lisa)/2)-1]+lisa[int(len(lisa)/2)])/2
    return lisa[int(len(lisa)/2)]
    

li=[5,1,7,2,8,2]
li2=[2,4,73,1,7]
li3=[5,1,7,2,8,2,2,4,73,1,7]
li4=[5,1,7,2,8,2,2,4,73,1,7,7]
print(srodek(li),srodek(li2),srodek(li3),srodek(li4))
