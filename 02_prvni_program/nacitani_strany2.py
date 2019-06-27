"""
Dlouha verze prikladu z materialu
"""

strana = float(input('Zadej stranu čtverce v centimetrech: '))
kladne = strana > 0
if kladne:
    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
else:
    print('Strana musí být kladná, jinak z toho nebude čtverec!')

print('Děkujeme za použití geometrické kalkulačky.')