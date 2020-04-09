plik=open("cw4_zad1.txt","w+")
[plik.write(str(x)+" ") for x in range(1,101) if x%4==0]
plik.close()
