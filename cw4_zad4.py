class NaZakupy():
    nazwa_produktu=""
    ilosc=0
    jednostka_miary=""
    cena_jed=0

    def __init__(self, np, il, jm, c):
        self.nazwa_produktu=np
        self.ilosc=il
        self.jednostka_miary=jm
        self.cena_jed=c

    def wyswietl_produkt(self):
        print("Nazwa produktu: ",self.nazwa_produktu)
        print("Ilosc: ",self.ilosc)
        print("Jednostka miary: ",self.jednostka_miary)
        print("Cena jednostkowa: ",self.cena_jed)

    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary,sep=" ")

    def ile_kosztuje(self):
        print(self.ilosc*self.cena_jed)


P1=NaZakupy("jablko",3,"kg",2.50)
P1.wyswietl_produkt()
P1.ile_kosztuje()
P1.ile_produktu()