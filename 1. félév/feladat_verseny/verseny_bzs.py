szotarlista = []

with open ("nevek.txt", "r", encoding="utf-8") as filebe:
    sorok = filebe.read().splitlines()

    for i in range (1, len (sorok)):
        nev = sorok[i].strip()
        szotarlista.append(nev)

    print("1. feladat:")
    print (f"Ebben az évben összesen {i} diák jelentkezett a versenyre.")

Knevlista = []
for i in range (1, len (nev)):
    if nev.startswith('K'):
        Knevlista.append(nev)
    print (f"A következő nevek kezdődnek K betűvel: {Knevlista})