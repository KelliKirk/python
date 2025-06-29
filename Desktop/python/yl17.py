# Kirjutage funktsioon leia_paarisarvud(algus, lõpp), mis:

# Võtab kaks parameetrit: algus ja lõpp (kaasa arvatud)
# Leiab kõik paarisarvud selles vahemikus
# Tagastab listi leitud paarisarvudega
# Kui paarisarve ei ole, tagastab tühja listi

# Näited:

# leia_paarisarvud(1, 10) peaks tagastama [2, 4, 6, 8, 10]
# leia_paarisarvud(5, 7) peaks tagastama [6]
# leia_paarisarvud(1, 1) peaks tagastama []

def leia_paarisarvud(algus, lõpp):

    paarisarvud = []

    for i in range(algus, lõpp+1):
        if i % 2 == 0:
         paarisarvud.append(i)  # Lisab paarisarvu listi
        
    
    return paarisarvud  # Tagastab listi alles tsükli lõppedes

# Funktsiooni kutsumine

tulemus = leia_paarisarvud(10, 20)

print(tulemus)