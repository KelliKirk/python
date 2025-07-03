# Loo abstraktne klass Kujund, mis:

# Omab abstraktseid meetodeid: arvuta_pindala() ja arvuta_ümbermõõt()
# Tavaline meetod info() - kuvab "See on kujund"

# Loo alamklassid:

# Ristkülik(Kujund) - võtab laiuse ja pikkuse
# Ring(Kujund) - võtab raadius (π ≈ 3.14)

# Mõlemad peavad implementeerima abstraktseid meetodeid.

from abc import ABC, abstractmethod

class Kujund(ABC):

     @abstractmethod
     def arvuta_pindala(self):
        pass
    
     @abstractmethod
     def arvuta_ümbermõõt(self):
        pass
    
     def info(self):
        print("See on kujund")

class Ristkülik(Kujund):
    def __init__(self, laius, pikkus):
        self.laius = laius
        self.pikkus = pikkus

    def arvuta_pindala(self):
            return self.laius * self.pikkus
        
    def arvuta_ümbermõõt(self):
            return 2 * (self.laius + self.pikkus)

class Ring(Kujund):
    def __init__(self, raadius):
        self.raadius = raadius
        self.pi = 3.14

    def arvuta_pindala(self):
        return self.pi * self.raadius ** 2
    
    def arvuta_ümbermõõt(self):
        return 2 * self.pi * self.raadius
    
ristkülik = Ristkülik(5, 10)
print(f"Ristküliku pindala: {ristkülik.arvuta_pindala()}")
print(f"Ristküliku ümbermõõt: {ristkülik.arvuta_ümbermõõt()}")

ring = Ring(3)
print(f"Ringi pindala: {ring.arvuta_pindala()}")
print(f"Ringi ümbermõõt: {ring.arvuta_ümbermõõt()}")

kujundid = [ristkülik, ring]
for kujund in kujundid:
    kujund.info()
    print(f"Pindala: {kujund.arvuta_pindala()}")
    print("---")


