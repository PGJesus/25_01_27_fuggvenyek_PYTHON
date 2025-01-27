"""4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!"""

def legrövidebb_szo(szo_lista):
    legrovidebb_szo = szo_lista[0]
    for szo in szo_lista:
        if len(szo) < len(legrovidebb_szo):
            legrovidebb_szo = szo
    return legrovidebb_szo

szavak = []
szam = int(input("Hány szót szeretnél megadni? "))

for i in range(szam):
    szo = input(f"{i+1}.")
    szavak.append(szo)

legrovidebb = legrövidebb_szo(szavak)
print(f"A legrövidebb szó: {legrovidebb}")

