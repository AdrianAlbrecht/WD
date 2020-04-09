class aryt():
    a1=0
    r=0
    ile=0


    def wyswietl_dane(self):
        print("Pierwszy wyraz ciagu: ",self.a1)
        print("Roznica: ", self.r)
        print("Ilosc: ", self.ile)

    def pobierz_elementy(self, a, r):
        self.a1=a
        self.r=r

    def pobierz_parametry(self, a, r, ile):
        self.a1=a
        self.r=r
        self.ile=ile
        return self.a1+self.r*(self.ile-1)

    def policz_sume(self):
        return ((self.a1+(self.a1+self.r*(self.ile-1)))/2)*self.ile

    def policz_elementy(self):
        for i in range(self.ile):
            print("a_",i+1,": ",self.a1+self.r*(i),sep="", end=" ")


c1=aryt()
c1.wyswietl_dane()
c1.pobierz_elementy(1,2)
c1.wyswietl_dane()
print(c1.pobierz_parametry(1,2,3))
c1.wyswietl_dane()
print(c1.policz_sume())
c1.policz_elementy()
