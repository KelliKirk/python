# Loo klass Kalkulaator, mis:

# Hoiab meeles viimast tulemust (algväärtus 0)
# Meetod liida(arv) - liidab arvu tulemusele
# Meetod lahuta(arv) - lahutab arvu tulemusest
# Meetod korruta(arv) - korrutab tulemust arvuga
# Meetod jaga(arv) - jagab tulemuse arvuga (kasuta try/except!)
# Meetod tulemus() - tagastab praeguse tulemuse
# Meetod nulli() - nullib tulemuse

class Kalkulaator:
    def __init__(self):
        self.tulemus_väärtus = 0
    
        
    def liida(self, arv):
        self.tulemus_väärtus += arv

    def lahuta(self, arv):
        self.tulemus_väärtus -= arv

    def korruta(self, arv):
        self.tulemus_väärtus *= arv

    def jaga(self, arv):
        try:
            self.tulemus_väärtus /= arv

        except ZeroDivisionError:
                print("Nulliga ei saa jagada!")

    def nulli(self):
        self.tulemus_väärtus = 0

    def tulemus (self):
      return self.tulemus_väärtus
    
calc = Kalkulaator()

calc.liida(5)
print(calc.tulemus())

calc.lahuta(2)
print(calc.tulemus())

calc.korruta(3)
print(calc.tulemus())

calc.jaga(4)
print(calc.tulemus())

calc.jaga(0)
print(calc.tulemus())

calc.nulli()
print(calc.tulemus())