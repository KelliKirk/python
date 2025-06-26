# Ülesanne: Loo lemmiklooma info koguja
# Kirjuta programm, mis:
# Küsib kasutaja nime
# Küsib tema lemmiklooma nime
# Küsib looma vanust (kontrolli, et oleks number ja mõistlik vanus 0-30)
# Küsib looma tüüpi (koer, kass, hamster, vms)
# Arvutab välja, mitu aastat on loom "inimese aastates" (kasuta valemit: looma vanus × 7)
# Kuvab kõik andmed koos mingi toreda kommentaariga

print("Tere tulemast lemmiklooma info kogujasse! 🐾")
print()

nimi = input("Mis on sinu nimi?")
looma_nimi = input("Mis on sinu lemmiklooma nimi?")
looma_vanus = int(input("Kui vana on su lemmikloom?"))
looma_liik = input("Sisesta oma looma liik (kass, koer, muu): ")

inimese_aastad = looma_vanus * 7

print()
print("--- SINU LEMMIKLOOMA INFO ---")
print("Sinu nimi:", nimi)
print("Looma nimi:", looma_nimi) 
print("Looma vanus:", looma_vanus, "aastat")
print("Looma liik:", looma_liik)
print("Inimese aastates:", inimese_aastad, "aastat")
print()
print("Tore loomake! 😊")

