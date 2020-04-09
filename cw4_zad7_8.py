class Robaczek():
    x=0
    y=0
    krok=1


    def __init__(self, x, y, k):
        self.x=x
        self.y=y
        self.krok=k

    def ile_w_gore(self, ile):
        self.y+=ile*self.krok
    
    def ile_w_dol(self, ile):
        self.y-=ile*self.krok

    def ile_w_prawo(self, ile):
        self.x+=ile*self.krok
    
    def ile_w_lewo(self, ile):
        self.x-=ile*self.krok

    def pokaz_gdzie_jestes(self):
        print("X: ",self.x,", Y: ",self.y)

    #zad8
    def __del__(self):
        del self.x
        del self.y
        del self.krok
        print("Zabiles robaczka :(")


Andrzej=Robaczek(0,0,3)
Andrzej.pokaz_gdzie_jestes()
Andrzej.ile_w_gore(3)
Andrzej.pokaz_gdzie_jestes()
Andrzej.ile_w_dol(2)
Andrzej.pokaz_gdzie_jestes()
Andrzej.ile_w_prawo(7)
Andrzej.pokaz_gdzie_jestes()
Andrzej.ile_w_lewo(4)
Andrzej.pokaz_gdzie_jestes()
#zad8
Andrzej="Juz nie robaczek"
print(Andrzej)
Andrzej=Robaczek(1,1,1)
