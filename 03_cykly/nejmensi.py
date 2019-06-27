"""
Určite nejmenší číslo z n zadaných,
volá pdb.set_trace() - ukázka debugování
"""

import pdb

pdb.set_trace()
n = int(input("Zadejte pocet cisel: "))


nejmensi = float(input("Zadejte cislo: "))
for i in range(n - 1):
    cislo = float(input("Zadejte cislo: "))
    print(cislo)
    if cislo < nejmensi:
        nejmensi = cislo


print("Nejmensi cislo bylo: ", nejmensi)
