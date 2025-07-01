# Kirjutage funktsioon loo_raamat(pealkiri, autor, lehekülgi), mis tagastab sõnastiku raamatu andmetega. Siis looge 2 raamatut ja printibe nende pealkirjad.

def loo_raamat(pealkiri, autor, lehekülgi):
    raamat = {
        "pealkiri": pealkiri,
        "autor": autor,
        "lehekülgi": lehekülgi
    }

    return raamat

videvik = loo_raamat("Videvik", "Stephenie Meyer", 300)
vanamees = loo_raamat("Vanamees ja meri", "Ernst Hemingway", 106)

print(videvik)
print(vanamees)

# ainult pealkirjade väljastamine:

# print(videvik["pealkiri"])      # "Videvik"
# print(vanamees["pealkiri"])     # "Vanamees ja meri"

# Või tsükliga:
# raamatud = [videvik, vanamees]
# for raamat in raamatud:
    # print(raamat["pealkiri"])