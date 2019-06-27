# -*- coding: utf-8 -*-
"""
V tehle verzi nevoli pocitac tah vzdy stejne nahodne.
"""
from random import randrange

tah_cloveka = input("Kámen, nůžky nebo papír?: ")

cislo = randrange(9)
if cislo <= 2:
    tah_pocitace = "kámen"
    print("Počítač hází kámen.")
elif cislo >= 7:
    tah_pocitace = "nůžky"
    print("Počítač hází nůžky.")
else:
    tah_pocitace = "papír"
    print("Počítač hází papír.")

vyhra_pocitace =  (tah_pocitace == "nůžky" and tah_cloveka == "papír") or \
                  (tah_pocitace == "kámen" and tah_cloveka == "nůžky") or \
                  (tah_pocitace == "papír" and tah_cloveka == "kámen")

if tah_pocitace == tah_cloveka:
   print("Plichta")
elif vyhra_pocitace:
    print("Pocitac vyhral!")
else:
    print("Vyhrali jste!")
