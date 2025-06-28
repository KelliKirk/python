# Kirjuta programm, mis küsib kasutajalt numbreid seni, kuni ta sisestab numbri 0. Programm peaks:

# Kui number on positiivne: "Positiivne number!"
# Kui number on negatiivne: "Negatiivne number!"
# Kui number on 0: "Lõpetan!" ja lõpetab tsükli
# Lõpus näita, mitu numbrit kokku sisestati (ilma 0-ta)

loendur = 0

while True:
    number = int(input("Sisesta number: "))
    loendur += 1

    if number == 0:
        print("Lõpetan")
        break

    elif number > 0:
        print ("Positiivne number")

    else:
        print ("Negatiivne number")