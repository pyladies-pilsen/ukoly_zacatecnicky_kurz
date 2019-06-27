
"""
Tohle je verze s pokrocilimi konstrukcemi, podivej se na ni az ke konci kurzu.
"""
from random import randint


moznosti = ["kámen", "nůžky", "papír"]
tah_pocitace = moznosti[randint(0, 2)]
tah_cloveka = input("kámen, nůžky nebo papír? ")

print(tah_pocitace)
if tah_cloveka == tah_pocitace:
    print("Plichta.")
elif ((tah_pocitace == "nůžky" and tah_cloveka == "papír") or
      (tah_pocitace == "kámen" and tah_cloveka == "nůžky") or
      (tah_pocitace == "papír" and tah_cloveka == "kámen")):
    print("Počítač vyhrál.")
elif tah_cloveka in moznosti:
    print("Vyhral jsi, gratuluji!")
else:
    print('Nerozumím, takhle se to nehraje.')

