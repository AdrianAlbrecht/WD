class Samogloski:
    __samogloski={"a","e","y","i","o","u"}

    def __init__(self, slowo):
        if isinstance(slowo,str):
            self.slowo = slowo
        else:
            self.slowo=str(slowo)
        self.ind = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.ind +=1
        if self.ind >= len(self.slowo):
            raise StopIteration
        if self.slowo[self.ind] in Samogloski.__samogloski:
            return self.slowo[self.ind]

Klaw=Samogloski("msnfheiucbsnwqbixiwnbxiwqxnwq")
lets=iter(Klaw)
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
print(next(lets))
more=Samogloski(454353454)
let=iter(more)
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))
print(next(let))