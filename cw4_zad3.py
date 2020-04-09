with open("cw4_zad3.txt", "w+") as plik:
    plik.write("Pierwsza linijka tekstu\n")
    plik.write("Druga linijka tekstu\n")
    plik.write("Trzecia linijka tekstu\n")
    plik.seek(0,0)
    for linia in plik:
        print(linia, end="")