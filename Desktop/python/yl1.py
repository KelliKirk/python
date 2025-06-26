# ÜLESANNE 1: Loo järgmised muutujad ja väljasta nende tüübid:
# - raamatu_pealkiri (string): "Harry Potter"
# - lehekylgede_arv (täisarv): 350
# - hind (ujukomaarv): 15.99
# - on_saadaval (boolean): True
# - autorid (nimekiri): ["J.K. Rowling"]

# SINU KOOD SIIA:
raamatu_pealkiri = "Harry Potter"
lehekylgede_arv = 350
hind = 15.89
on_saadaval = True
autorid = ["J.K. Rowling"]

# Väljasta iga muutuja väärtus ja tüüp
# print(f"Pealkiri: {} (tüüp: {})")
# jne...

print(f"Raamatu pealkiri: {raamatu_pealkiri} (tüüp: {type(raamatu_pealkiri)})")
print(f"Lehekülgede arv: {lehekylgede_arv} (tüüp: {type(lehekylgede_arv)})")
print(f"Hind: {hind} (tüüp: {type(hind)})")
print(f"On saadaval: {on_saadaval} (tüüp: {type(on_saadaval)})")
print(f"Autorid: {autorid} (tüüp: {type(autorid)})")

print("\n" + "="*50 + "\n")