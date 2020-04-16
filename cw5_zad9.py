def parzyste(slowo):
    for ind in range(0,len(slowo)-1,2):
        yield slowo[ind]

Imie=parzyste("Elżbieta")
print(next(Imie))
print(next(Imie))
print(next(Imie))
print(next(Imie))
print(next(Imie))