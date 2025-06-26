# ÜLESANNE 2: Kohviku arve kalkulaator
# Loo muutujad järgmistele andmetele:
# - kohvi_hind: 2.5 eurot
# - saia_hind: 1.2 eurot
# - ostetud_kohvid: 2 tükki
# - ostetud_saiad: 3 tükki

# SINU KOOD SIIA:
kohvi_hind = 2.5
saia_hind = 1.2
ostetud_kohvid = 2
ostetud_saiad = 3

# Arvuta:
kohvi_kokku = 2 * 2.5
sai_kokku = 3 * 1.2  
arve = kohvi_kokku + sai_kokku
# - lisa veel 1 kohv ja arvuta uus kogusumma
ostetud_kohvid += 1  # nüüd on 3 kohvi, += operaator lisab alati ühe juurde
uus_kokku = (ostetud_kohvid + kohvi_hind) + sai_kokku

print(arve)     # arve enne
print(uus_kokku) # arve pärast

# Kui soovime lisada selgituse:
print(f"Algne arve: {arve}€")
print(f"Uus arve: {uus_kokku}€")