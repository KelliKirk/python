# Kirjuta programm, mis küsib kasutajalt numbrit ja ütleb:

# Kui number on 0: "Null"
# Kui number on positiivne: "Positiivne arv"
# Kui number on negatiivne: "Negatiivne arv"

arv = int(input("Sisesta arv: "))

if arv == 0:
 print ("Null")

elif arv > 0:
 print ("Positiivne arv")

elif arv < 0:
 print ("Negatiivne arv")