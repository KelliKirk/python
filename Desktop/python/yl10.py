# Kirjuta programm, mis küsib kasutajalt numbreid ja loeb, mitu numbrit sisestati, kuni kasutaja sisestab -1.
# Tulemus peaks näitama, mitu numbrit kokku sisestati (ilma -1-ta).

loendur = 0
number = int(input("Sisesta number (-1 lõpetamiseks): "))

while number != -1:
    loendur += 1
    number = int(input("Sisesta number (-1 lõpetamiseks): "))

print(f"Numbreid on: {loendur}")