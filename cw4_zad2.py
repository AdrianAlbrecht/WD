with open("cw4_zad1.txt", "r") as plik:
    for linia in plik:
        numery= list(linia.split(" "))
        for i in numery:
            print(i, end=" ")
            
#rozdzielenie na liste, żeby dostać się do pojedynczych wartości dla własnej praktyki- zdaję sobie sprawę,
#że można było prościej
