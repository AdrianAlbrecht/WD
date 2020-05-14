#ściezka jakiej musiałem użyć do pliku, aby mi zadziałało: './Kolos_nr_1/z8.txt'
def z8():
    plik=open('z8.txt','r')
    imiona={}
    for line in plik:
        li=line.split("\n")
        if li[0] in imiona.keys():
            imiona[str(li[0])]+=1
        else:
            imiona[str(li[0])]=1
    for key,value in imiona.items():
        print("{}: {}".format(key,value))
    plik.close()

z8()