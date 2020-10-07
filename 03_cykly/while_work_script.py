# -*- coding: utf-8 -*-
#  Pracovní skript k cyklu while

# Cyklus for se hodí pokud známe počet opakování před
# začátkem cyklu. Co když ale chceme něco opakovat, dokud
# akci neukončí uživatel?

pokracuj = "ano"
while pokracuj == "ano":
    pokracuj = input("Mám pokračovat? ")
print("Konec")

print()
# Někdy se hodí ukončit cyklus v půlce.
pokracuj = "ano"
while pokracuj == "ano":
    print("Teď se zeptám, jestli mám pokračovat.")
    pokracuj = input("Mám pokračovat? ")
    if pokracuj != "ano":
        break
print("Konec")

print()
# Často se spolehneme jen na to.
while True:
    print("Teď se zeptám, jestli mám pokračovat.")
    pokracuj = input("Mám pokračovat? ")
    if pokracuj != "ano":
        break
print("Konec")

# while True: ... je nekonečný cyklus
while True:
    print("Nikdy neodstoupí, nikdy!")



