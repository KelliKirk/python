# Kirjuta programm, mis küsib kasutajalt temperatuuri (Celsius) ja ütleb:

# Kui alla 0: "Külm, jää"
# Kui 0-10: "Jahe"
# Kui 11-20: "Mõnus"
# Kui 21-30: "Soe"
# Kui üle 30: "Kuum"

temperatuur = int(input("Sisesta temperatuur: "))

if temperatuur < 0:
    print ("Külm, jää")

elif temperatuur >= 0 and temperatuur <= 10:
    print ("Jahe")

elif temperatuur >= 11 and temperatuur <= 20:
    print("Mõnus")

elif temperatuur >= 21 and temperatuur <= 30:
    print ("Soe")

elif temperatuur > 30:
    print ("Kuum")