# Kirjuta programm, mis küsib kasutajalt nädalapäeva numbrit (1-7) ja ütleb:

# 1: "Esmaspäev"
# 2: "Teisipäev"
# 3: "Kolmapäev"
# 4: "Neljapäev"
# 5: "Reede"
# 6: "Laupäev"
# 7: "Pühapäev"
# Kõik muud numbrid: "Vale number! Sisesta 1-7"

paev = int(input("Sisesta number 1-7: "))

if paev == 1:
    print("Esmaspäev")

elif paev == 2:
    print ("Teisipäev")

elif paev == 3:
    print ("Kolmapäev")

elif paev == 4:
    print ("Neljapäev")

elif paev == 5:
    print ("Reede")

elif paev == 6:
    print ("Laupäev")

elif paev == 7:
    print ("Pühapäev")

else:
    print ("Vale number! Sisesta 1-7!")