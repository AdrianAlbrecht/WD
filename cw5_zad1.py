class Material():
    rodzaj=""
    dlugosc=0
    szerokosc=0

    def __init__(self,r,d,s):
        self.rodzaj=r
        self.dlugosc=d
        self.szerokosc=s
    def wyswietl_nazwe(self):
        print(self.__class__.__name__)


class Ubranie(Material):
    rozmiar=""
    kolor=""
    dla_kogo=""

    def wyswietl_dane(self):
        print("{} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo))


class Sweter(Ubranie):
    rodzaj_swetra=""

    def wyswietl_dane(self):
        print("{} {} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj_swetra))


Jedwab=Material("naturalny",24,53)
Jedwab.wyswietl_nazwe()
Koszulka=Ubranie("naturalny",50,23)
Koszulka.rozmiar="XXL"
Koszulka.kolor="czarny"
Koszulka.dla_kogo="Maciek"
Koszulka.wyswietl_dane()
Koszulka.wyswietl_nazwe()
Golfik=Sweter("naturalny",90,45)
Golfik.rodzaj_swetra="Rozpinany"
Golfik.kolor="Żółty"
Golfik.rozmiar="M"
Golfik.dla_kogo="Buldog"
Golfik.wyswietl_dane()
Golfik.wyswietl_nazwe()

