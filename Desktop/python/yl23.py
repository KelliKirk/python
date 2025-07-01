# Kirjuta funktsioon teisenda_temperatuur(), mis:

# Küsib kasutajalt Celsiuse kraade
# Teisendab need Fahrenheiti kraadideks (valem: F = C * 9/5 + 32)
# Kuvab tulemuse kujul: "25°C on 77.0°F"
# Kasutab try/except blokki, et käsitleda juhtumeid, kus kasutaja sisestab midagi muud kui numbri
# Kui sisestus pole number, kuva: "Viga: Palun sisesta kehtiv number!"

# Lisaülesanne: Lisa kontroll, et kui temperatuur on alla -273.15°C (absoluutne null), siis kuva hoiatus: "Hoiatus: See temperatuur on võimatu!"

def teisenda_temperatuur():
    try:
      celsius = float(input("Sisesta temperatuur Celsiustes: "))
      fahrenheit = celsius * 9/5 + 32

      print(f"{celsius} C on {fahrenheit} F.")

      if celsius < -273.15:
         print("Hoiatus: See temperatuur on võimatu!")

    except ValueError:
       print("Viga: Palun sisesta kehtiv number!")

teisenda_temperatuur()