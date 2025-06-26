# Loo lihtne sisseostude nimekiri programm:
# 1. Loo tühi nimekiri
# 2. Lisa tsükliga 3 toodet nimekirja
# 3. Väljasta kogu nimekiri

print("Sisseostude nimekiri:")

# SINU KOOD SIIA:
sisseostud = []

for i in range(3):
 toode = input(f"Sisesta {i+1}. toode: ")
 sisseostud.append(toode)

print("\nSinu sisseostude nimekiri:")
for i, toode in enumerate(sisseostud, 1):
   print(f"{i}. {toode}")

print("\n" + "="*50 + "\n")