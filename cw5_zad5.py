class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


mariusz= Osoba("Mariusz", "Mortens")
jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(mariusz.przedstaw_sie())
print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

print(isinstance(mariusz,Osoba))
print(isinstance(mariusz,Pracownik))
print(isinstance(mariusz,Menadzer))
print("")
print(isinstance(jozek,Osoba))
print(isinstance(jozek,Pracownik))
print(isinstance(jozek,Menadzer))
print("")
print(isinstance(adrian,Osoba))
print(isinstance(adrian,Pracownik))
print(isinstance(adrian,Menadzer))
print("")
print(issubclass(Osoba,Osoba))
print(issubclass(Pracownik,Osoba))
print(issubclass(Menadzer,Osoba))
print("")
print(issubclass(Osoba,Pracownik))
print(issubclass(Pracownik,Pracownik))
print(issubclass(Menadzer,Pracownik))
print("")
print(issubclass(Osoba,Menadzer))
print(issubclass(Pracownik,Menadzer))
print(issubclass(Menadzer,Menadzer))
