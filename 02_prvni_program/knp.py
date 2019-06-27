"""
Ucesana verze hry kamen, nuzky, papir s pouzitim 'or' a 'and'
"""
from random import randrange


cislo = randrange(3)
if cislo == 0:
    tah_pocitace = "kámen"
elif cislo == 1:
    tah_pocitace = "nůžky"
elif cislo == 2:
    tah_pocitace = "papír"


tah_cloveka = input("kámen, nůžky nebo papír? ")

import ipdb; ipdb.set_trace()

print(tah_pocitace)
if tah_cloveka == tah_pocitace:
    print("Plichta.")
elif ((tah_pocitace == "nůžky" and tah_cloveka == "papír") or
      (tah_pocitace == "kámen" and tah_cloveka == "nůžky") or
      (tah_pocitace == "papír" and tah_cloveka == "kámen")):
    print("Počítač vyhrál.")
elif ((tah_cloveka == "nůžky") or
      (tah_cloveka == "kámen") or
      (tah_cloveka == "papír") ):
    print("Vyhral jsi, gratuluji!")
else:
    print('Nerozumím, takhle se to nehraje.')
