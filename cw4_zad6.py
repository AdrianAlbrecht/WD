class Slowa():
    slowo1="a"
    slowo2="b"

    
    def __init__(self,x,y):
        self.slowo1=x
        self.slowo2=y

    def sprawdz_czy_palindrom(self):
        print(self.slowo1, end=" ")
        if self.slowo1!=self.slowo1[::-1]:
            print("nie ",end="")
        print("jest palindromem.")
        print(self.slowo2, end=" ")
        if self.slowo2!=self.slowo2[::-1]:
            print("nie ",end="")
        print("jest palindromem.")

    def sprawdz_czy_metagramy(self):
        czy=False
        if len(self.slowo1)==len(self.slowo2):
            Npl=0
            for i in range(len(self.slowo1)):
                if self.slowo1[i]!=self.slowo2[i]:
                    Npl+=1
            if Npl==1:
                czy=True
        if czy:
            print("Slowa sa metagramami.")
        else:
            print("Slowa nie sa metagramami.")

    def sprawdz_czy_anagramy(self):
        czy=True
        if len(self.slowo1)==len(self.slowo2):
            napis = self.slowo2
            for znak in self.slowo1:
                if znak in napis:
                    i = napis.index(znak)
                    napis = napis[:i]+napis[i+1:]
                else:
                    czy=False
        else:
            czy=False
        if czy:
            print("Slowa sa anagramami.")
        else:
            print("Slowa nie sa anagramami.")   
            

    def wyswietl_wyrazy(self):
        print(self.slowo1, end=" ")
        print(self.slowo2)


Zestaw=Slowa("sadsad","kamilslimak")
Zestaw.wyswietl_wyrazy()
Zestaw.sprawdz_czy_palindrom()
Zestaw=Slowa("tata","mama")
Zestaw.sprawdz_czy_metagramy()
Zestaw=Slowa("tata","mata")
Zestaw.sprawdz_czy_metagramy()
Zestaw=Slowa("tata","matasdsdsd")
Zestaw.sprawdz_czy_metagramy()
Zestaw=Slowa("tama","mata")
Zestaw.sprawdz_czy_anagramy()
Zestaw=Slowa("tama","tata")
Zestaw.sprawdz_czy_anagramy()
Zestaw=Slowa("tama","mataa")
Zestaw.sprawdz_czy_anagramy()