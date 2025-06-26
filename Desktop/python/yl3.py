# ÜLESANNE 3A: FOR tsükkel
# Väljasta paarisarvud 2-st 10-ni (2, 4, 6, 8, 10)
print("Paarisarvud 2-st 10-ni:")

# SINU KOOD SIIA:
for i in range(2, 11, 2): # Miks? Sest range'il on start, stop ja step. Start on 2 (alustame sellest numbrist), stop on 11 (lõpetame enne numbrit 11, seega viimane number on 10) ja step on 2 (iga sammu pikkus on 2, seega väljastatakse paarisarvud). 
  print(f"Paarisarv: {i}")

print()

# ÜLESANNE 3B: FOR tsükkel nimekirjaga
# Loo nimekiri 5 linna nimega ja väljasta iga linn
linnad = ["Tartu", "Tallinn", "Elva", "Jõgeva", "Valga"]  

print("Eesti linnad:")
# SINU KOOD SIIA:
for linn in linnad:
   print(f"Linn: {linnad}")

print()

# ÜLESANNE 3C: WHILE tsükkel
# Loo lihtne arvamismäng: alusta numbriga 1 ja korrata,
# kuni jõuad numbri 20-ni, aga väljasta ainult numbrid, 
# mis jagunevad 3-ga

print("Numbrid, mis jagunevad 3-ga (1-20):")

# SINU KOOD SIIA:
arv = 1
while arv <= 20:
    if arv % 3 == 0:  
        print(f"Jagub 3-ga: {arv}")
    arv += 1  # ← See peab olema IF-ist väljas!

# ÜLESANNE 3D: Arvutused tsüklis
# Loo nimekiri hinnetega ja arvuta keskmine
hinded = [1, 2, 3, 4, 5]  # lisa siia 5 hinnet (1-5)

print("Hinnete analüüs:")
# SINU KOOD SIIA:
summa = 0
for hinne in hinded:
   summa += hinne
   print(f"Lisasin hinde {hinne}, summa: {summa}")

keskmine = summa / len(hinded)
print(f"Keskmine hinne: {keskmine:.2f}")

print("\n" + "="*50 + "\n")