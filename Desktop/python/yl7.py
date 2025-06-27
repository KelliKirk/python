# Kirjuta programm, mis küsib kasutajalt arvu n ja arvutab välja kõigi numbrite summa 1-st n-ni.
# Näiteks kui kasutaja sisestab 5, siis programm peaks arvutama: 1 + 2 + 3 + 4 + 5 = 15

n = int(input("Sisesta arv: "))

summa = 0

for i in range(1, n+1): # See on selleks, et saada numbrid  1-st n-ni
    summa += i

print(summa)
