def rownolegle_czy_prostopadle(a,b,c,d):
    if a==c:
        print("Rownolegle")
    elif a*c==-1:
        print("Prostopadle")
    else:
        print("Ani rownolegle ani prostopadle")
rcp=rownolegle_czy_prostopadle
rcp(float(input("Podaj a1: ")),float(input("Podaj b1: ")),float(input("Podaj a2: ")),float(input("Podaj b2: ")))