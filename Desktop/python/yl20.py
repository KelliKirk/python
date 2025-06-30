# Kirjutage:

# Kaks funktsiooni: lisa_hüüumärk(tekst) ja tee_suurtähed(tekst)
# Põhifunktsioon muuda_teksti(tekst, muutmise_funktsioon)

# Funktsioon peaks saama kasutada nii:

# muuda_teksti("tere", lisa_hüüumärk) → "tere!"
# muuda_teksti("tere", tee_suurtähed) → "TERE"

def lisa_hüüumärk(tekst):
    return f"{tekst}!"

def tee_suurtähed(tekst):
    return tekst.upper()

def muuda_teksti(tekst, muutmise_funktsioon):
    vastus = muutmise_funktsioon(tekst)
    return vastus

print(muuda_teksti("appi", lisa_hüüumärk))

print(muuda_teksti("appi", tee_suurtähed))