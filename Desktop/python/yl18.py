# Ülesanne 1: Kirjutage liida_kõik(arvud) - liidab kõik listi arvud kokku ja tagastab summa.


def liida_koik(arvud):
    tulemus = 0
    for arv in arvud:
        tulemus = tulemus + arv
    return tulemus

print (liida_koik([1, 2, 3]))