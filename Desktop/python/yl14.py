# Kirjuta programm, mis küsib kasutajalt 6 KORDA sisestada ühe arvu (kokku saad 6 erinevat arvu). Programm kontrollib iga sisestatud arvu kohta, kas see on paaris või paaritu, ja loendab, mitu paaris arvu kokku sisestati.
# Programm peaks näitama iga numbri kohta, kas see on paaris või paaritu, ja lõpus ütlema, mitu paaris numbrit kokku oli.



loendur = 0

for i in range(6):
    arv = int(input("Sisesta arv: "))
    
    if arv % 2 == 0:
        loendur += 1
        print("Paarisarv")  # <-- IF-i SEES
    else:
        print("Paaritu arv")  # <-- ELSE peab olema sama tasandil IF-iga

print(f"Paaris numbreid oli: {loendur}")