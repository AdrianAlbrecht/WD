def zmiana(lista):
    return [[li[x][y] for y in range(2,-1,-1)]for x in range(3)]        

li=[[1,2,3],[4,5,6],[7,8,9]]
li_od=zmiana(li)
print(li)
print(li_od)