class Parzyste:
    def __init__(self, slowo):
        self.slowo = slowo
        self.ind = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.ind +=2
        if self.ind >= len(self.slowo):
            raise StopIteration
        return self.slowo[self.ind]

Imie=Parzyste("Nabuchodonozor")
nab=iter(Imie)
print(next(nab))
print(next(nab))
print(next(nab))
print(next(nab))
print(next(nab))
print(next(nab))
print(next(nab))
print(next(nab))
