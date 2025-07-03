# Loo vanemklass Töötaja, mis:

# Võtab nime ja palka konstruktoris
# Omab privaatset __palk muutujat
# Meetod näita_info() - kuvab nime ja palka
# Meetod _arvuta_boonused() - kaitstud meetod, tagastab 0

# Loo alamklass Müügiesindaja(Töötaja), mis:

# Lisab konstruktorisse müügimahu parameetri
# Ülekirjutab _arvuta_boonused() - tagastab müügimahu * 0.1
# Meetod kogu_sissetulek() - tagastab palga + boonused

class Töötaja:
    def __init__(self, nimi, palk):
        self.nimi = nimi
        self.__palk = palk

    def näita_infot(self):
          print(f"Nimi: {self.nimi}")   
          print(f"Palk: {self.__palk}")

    def _arvuta_boonused(self):
         return 0
    
    def saa_palk(self): 
        return self.__palk
    
class Müügiesindaja(Töötaja):
     def __init__(self, nimi, palk, müügimaht):
          super().__init__(nimi, palk)
          self.müügimaht = müügimaht

     def _arvuta_boonused(self):
         return self.müügimaht * 0.1
     
     def kogu_sissetulek(self):
         return self.saa_palk() + self._arvuta_boonused()

müüginaine = Müügiesindaja("Kati", 1200, 30)
print(müüginaine.kogu_sissetulek())
print(müüginaine.saa_palk())