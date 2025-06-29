# Kirjuta funktsioon kontrolli_vanust(vanus), mis:

# Tagastab "Laps" kui vanus alla 18
# Tagastab "Täiskasvanu" kui vanus 18-65
# Tagastab "Pensionär" kui vanus üle 65

vanus = int(input("Sisesta vanus: "))

def kontrolli_vanust(vanus):
    if vanus < 18:
        return ("Laps")

    elif vanus >= 18 and vanus <= 65:
        return ("Täiskasvanu")

    else:
        return ("Pensionär")

print(kontrolli_vanust(vanus))
