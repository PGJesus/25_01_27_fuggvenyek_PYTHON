"""2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!"""

def poz_v_neg(szam):
    if szam > 0:
        print("A szám pozitív.")
    elif szam < 0:
        print("A szám negatív.")
    else:
        print("A szám nulla.")

folyt = True

while folyt:
    bemenet = input("Adj meg egy számot: ")    
    if bemenet == "":
        folyt = False
    else:
        szam = float(bemenet)
        poz_v_neg(szam)

