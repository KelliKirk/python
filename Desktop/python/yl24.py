# Loo klass Õpilane, mis:

# Võtab konstruktoris nime ja vanuse
# Omab tühja hinnetete listi
# Meetod lisa_hinne(hinne) - lisab hinde (1-5)
# Meetod keskmine() - arvutab ja tagastab hinnete keskmise
# Meetod info() - kuvab õpilase nime, vanuse ja keskmise hinde

class Õpilane:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        self.hinded = []

    def lisa_hinne(self, hinne):
      if 1 <= hinne <= 5:  # Kontrollib, et hinne on 1-5 vahel
        self.hinded.append(hinne)
        print(f"Hinne {hinne} lisatud!")
      else:
        print("Hinne peab olema 1-5 vahel!")

    def keskmine(self):
       if len(self.hinded) == 0:
          return 0
       return sum(self.hinded) / len(self.hinded)
    
    def info(self):
         print(f"Nimi: {self.nimi}")   
         print(f"Vanus: {self.vanus}")         
         print(f"Keskmine hinne: {self.keskmine()}")  

 
õpilane_1 = Õpilane("Kelli", 32)
õpilane_1.lisa_hinne(3)
õpilane_1.lisa_hinne(5)

õpilane_2 = Õpilane("Kaisa", 31)
õpilane_2.lisa_hinne(4)
õpilane_2.lisa_hinne(5)

õpilane_1.info()
õpilane_2.info()