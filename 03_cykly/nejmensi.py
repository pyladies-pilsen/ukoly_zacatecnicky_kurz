"""
Určete nejmenší číslo z n zadaných.
"""

n = int(input("Zadejte pocet cisel: "))


nejmensi = float(input("Zadejte cislo: "))
for i in range(n - 1):
    cislo = float(input("Zadejte cislo: "))
    print(cislo)
    if cislo < nejmensi:
        nejmensi = cislo


print("Nejmensi cislo bylo: ", nejmensi)