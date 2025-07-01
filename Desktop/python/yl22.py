# Kirjutage funktsioon loe_fail(failinimi), mis loeb faili sisu ja printib selle välja.

# Faili loomine

with open("test.txt", "w", encoding="utf-8") as fail:
    fail.write("Tere maailm!\n")
    fail.write("See on test fail.\n")
    fail.write("Python on lahe.\n")

print("Fail loodud!")


# Failist lugemine

def loe_fail(failinimi):
    with open(failinimi, "r", encoding="utf-8") as fail:
        sisu = fail.read()
        print(sisu)

loe_fail("test.txt")