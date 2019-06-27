"""
Učite největší číslo z pěti zadaných
"""

n = 5

nej = float(input("Zadejte cislo> "))  # nacteme si prvni cislo, abychom meli s cim porovnavat
# Pozn.: kdyby uzivatel zadal jen jedno cislo tak to bude prave to nejvetsi.
for i in range(n-1):
    c = float(input("Zadejte cislo> "))
    if c > nej:  # kdyz je c vetsi tak nej nemuze byt nejvetsi
        nej = c  # tak si schovame to vetsi a jedem dal

print("Nejvetsi cislo bylo ", nej)
