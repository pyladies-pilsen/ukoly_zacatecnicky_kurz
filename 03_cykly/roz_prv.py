#!/usr/bin/env python
"""
Spočte rozklad na prvočísla
"""

c = int(input("Zadejte číslo> "))
print(c, '= ', end="")
prvocislo = 2
while c > 1:
    if c % prvocislo == 0:
        print(prvocislo, end="")
        c = c / prvocislo
        if c != 1:
            print('*', end="")
    elif prvocislo == 2:
        prvocislo += 1
    else:
        prvocislo += 2
print()
