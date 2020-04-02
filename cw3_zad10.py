def lista_zaupow(**klucz):
    print("Lista zakupow:\n")
    ile=0
    for i in klucz:
        print(i, klucz[i])
        ile+=klucz[i]
    print("\nIlosc produktow w sumie:",ile)
lista_zaupow(pomidor=5,olej=2,jablka=3,banany=5)