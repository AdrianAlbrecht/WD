def monotonicznosc(a,b):
    if a>0:
        print("Rosnaca")
    elif a==0:
        print("Stala")
    else:
        print("Malejaca")
c=int(input('Podaj a: '))
d=int(input('Podaj b: '))
mono=monotonicznosc
mono(c,d)