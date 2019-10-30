# Řešení opakovacích příkladů
# ---------------------------
# Soubor sice jde spustit, ale nedoporučuji to, prohlédni si řešení, pokud
# chceš nějaké vyzkoušet raději si ho zkopíruj. Zadání je v komentářích
# začinajících `#`, komentře k řešení jsou v trojitých uvozovkách: """
#
# 0. První program
#     Z0 Napiš program, který nám popřeje dobré ráno.

print("Dobré ráno, PyLaides!")

# 1. Proměnné
#     Z1 Napiš program, který spočítá a vypíše obvod a obsah čtverec se
#     stranou a = 256 a kruhu o stejném poloměru. Číslo 256 se v kódu smí
#     objevit jen jednou! Místo pí stačí použít hodnotu 3.14.

a = 256
print("Obvod krychle o straně", a, "je", 256 * 4)
print("Obsah krychle o straně", a, "je", 256**2)
print("Obvod kruhu o poloměru", a, "je", 2 * 3.14 * a)
print("Obsah kruhu o poloměru", a, "je", 3.14 * a**2)

#     Z2 Napiš program, který se zeptá uživatele na číslo a vypíše jeho třetí
#     mocninu.

cislo = float(input("Zadejte číslo: "))
print(cislo, "³ je ", cislo**3, sep="")

# 2. Větvení a porovnávání
#     Z1 Napiš program, který se zeptá uživatele na číslo a vypíše,
#     jestli bylo kladné nebo záporné. Nulu může program ignorovat.

cislo = float(input("Zadejte číslo: "))
if cislo > 0:
    print("Číslo bylo kladné")
elif cislo < 0:
    print("Číslo bylo záporné")
else:
    print("Nula.")

#     Z2 Napiš program, který se zeptá uživatele "Známe se?" a pokud uživatel
#     odpoví "ne", program se představí, jinak neudělá nic.

zname_se = input("Známe se?")
if zname_se == "ne":
    print("Ahoj Dave, já jsme HAL")

#     P1 Napiš program, který se zeptá uživatele na číslo a vypíše "Bingo!"
#     pokud je jeho třetí mocnina dělitelná třemi.

cislo = float(input("Zadejte číslo: "))
if cislo**3 % 3 == 0:
    print("Bingo!")

# 3. Cykly
#     Z1 Napiš program, který vypíše čísla od 0 do 19.

for i in range(20):
    print(i)

#     Z2 Napiš program, který bude neustále vypipsovat "... a dál?".

"""
# zakomentováno aby se dal program spustit a šli vyzkoušet i ostatní úkoly
while True:
    print("... a dál?")
"""

#     P1 Napiš program, který sečte všechny násobky čísla 7 menší než 100.

soucet = 0
for i in range(0, 100):
    if i % 7 == 0:
        soucet = soucet + 7
print("Součet:", soucet)

"""nebo optimalizovaná verze"""

soucet = 0
for i in range(0, 100, 7):
    soucet = soucet + 7
print("Součet:", soucet)

#     P2 Napiš program, který se bude ptát uživatele na čísla, dokud nezadá
#     "konec". Poté program vypíše průměr všech zadaných čísel.

soucet = 0
pocet = 0
cislo = 0
while cislo != "konec":
    cislo = input('Zadejte číslo nebo "konec": ')
    if cislo != "konec":
        soucet = soucet + float(cislo)
        pocet = pocet + 1
print("Prumer zadanych cisel byl:", soucet/pocet)

#     P3 Napiš program, který vypíše následující tabulku.
#         1 0 0 0
#         0 1 0 0
#         0 0 1 0
#         0 0 0 1

for i in range(4):
    for j in range(4):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

#     P3* Uprav program tak, aby se dala velikost tabulky snadno měnit.

velikost = 4
for i in range(velikost):
    for j in range(velikost):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
#
# 4. Funkce
#     Ke každé funkci napiš krátký program, který ji použije a výsledek vypíše.
#
#     Z1 Napiš funkci, která dostane jako argumenty dvě čísla, která sečte
#     a výsledek VYPÍŠE.


def vypis_soucet(x, y):
    print(x + y)


vypis_soucet(1, 2)

#     Z2 Napiš funkci, která dostane jako argumenty dvě čísla, která sečte
#     a výsledek VRÁTÍ.


def vrat_soucet(x, y):
    return x + y


vysledek = vrat_soucet(2, 3)
print(vysledek)

#     Z* Napiš funkci, která vypíše svůj první argument a druhý vrátí.


def vypis1_vrat2(arg1, arg2):
    print(arg1)
    return arg2


vraceny_argument = vypis1_vrat2(451, 666)
print("Obsah proměnné `vraceny_argument`: ", vraceny_argument)

#     Z3 Napiš funkci, která pomocí želvy nakreslí čtverec se dvěma nohama,
#     nějak takhle
#         ┌---┐
#         |   |
#         └---┘
#          └ └

#     P1 Napiš funkci, která bude mít jako argumenty dvě čísla `z` a `e` a vrátí
#     `z` umocněno na `e`, `e` musí být celé kladné číslo. Nepouživej
#     operátor `**` ale for cyklus.


def umocni(z, e):
    vysledek = 1
    for i in range(e):
        vysledek = vysledek * z
    return vysledek


print("Funguje umocnovani na nultou? ... ", umocni(3, 0))
print("Kontrola, 3³ by mělo být 27 ... ", umocni(3, 3))

#     P1* Doplň funkci o kontrolu jesli je `e` celé kladné číslo,
#     v takovém případě vrátí funkce nulu.


def umocni2(z, e):
    vysledek = 1
    if (e < 0) or (int(e) - e != 0):
        return 0
    for i in range(int(e)):
        vysledek = vysledek * z
    return vysledek


print("Při umocňování na 1.7 by měla vyjít 0 ...", umocni2(3, 1.7))
print("Při umocňování na -1 by měla vyjít 0 ...", umocni2(3, -1))
print("Umocňování na 3 by ale mělo dál fungovat ... ", umocni2(3, 3.0))

#     P2 Pomocí želvy nakresli stonožku, použij dvounohé čtverce.
#
#              ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐
#             <|   |-|   |-|   |-|   |-|   |-|   |-|   |-|   |- ...
#              └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └---┘
#               └ └   └ └   └ └   └ └   └ └   └ └   └ └   └ └

# 5. Řetězce
#     Ke každé funkci napiš krátký program, který ji použije a výsledek vypíše.
#
#     Z1 Napiš program, který se zeptá uživatele na řetězec znaků a vymění v něm
#     všechna písmena "s" za "f".

text = input("Zadejte text: ")
text = text.replace("s", "f")
print(text)

#     Z2 Napiš program, který vypíše text "Flat is better than nested." do
#     sloupečku:
#         F
#         l
#         a
#         .
#         .
#         .

text = "Flat is better than nested."
for znak in text:
    print(znak)

"""nebo dokonce"""

for znak in "Flat is better than nested.":
    print(znak)

#     Z3 Napiš program, který se zeptá nejprve na jméno a poté na příjmení
#     uživatele a poté vypíše jeho iniciály.

jmeno = input("Zadejte svoje jmeno: ")
prijmeni = input("Zadejte svoje příjmení: ")
print("Vaše iniciály jsou:", jmeno[0], prijmeni[0])

#     P1 Napiš funkci, která vrátí True pokud jako argument dostala buď prázdný
#     řetězec nebo pokud zadaný řetězec obsahuje písmeno "Y" nebo "y". Jinak
#     vrátí False.


def mam_pokracovat(odpoved):
    if (odpoved == "") or ("Y" in odpoved) or ("y" in odpoved):
        return True
    else:
        return False


print(mam_pokracovat("Yes"))

#     P2 Napiš funkci, která dostane jako argument číslo a vrátí řetězec
#     "Tvoje skóre je " na jehož konec připojí dané číslo.


def skore(cislo):
    return "Tvoje skore je " + str(cislo)


hlaska = skore(9000)
print(hlaska)

# 6. Soubory
#     Z1 Napiš program, který načte textový soubor a výpíše jeho obsah.

soubor = open("ukoly.txt", encoding="utf-8")
text = soubor.read()
print(text)

#     Z2 Napiš program, který řekne uživateli, aby zadal cokoliv a zapíše to do
#     souboru vystup.txt.

text = input("Zadjete neco: ")
vystupni_soubor = open("vystup.txt", "w", encoding="utf-8")
print(text, file=vystupni_soubor)
vystupni_soubor.close()

#     P1 Napiš program, který se zeptá uživatele na jméno souboru, načte jeho
#     obsah a nahradí všechny znaky ";" (středník) znakem pro prázdný řádek "\n"
#     a zapíše výsledek zpět od souboru. Pokud soubor žádné ";" neobsahuje,
#     program to oznámí.

jmeno_souboru = input("Zadejte jmeno souboru: ")
soubor = open(jmeno_souboru, encoding="utf-8")
text = soubor.read()
soubor.close()

if ";" in text:
    text = text.replace(";", "\n")
    vystupni_soubor = open(jmeno_souboru, "w", encoding="utf-8")
    print(text, file=vystupni_soubor)
    vystupni_soubor.close()
else:
    print("Soubor,", jmeno_souboru, 'neobsahuje žádné ";"')

#     P2 Zkopíruj si dvounohý čtverec z úkolu 4Z3 a vypiš stonožu do souboru.┌ ┌
#                                                                            | |
#        ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐ ┌---┐
#   ... -|   |-|   |-|   |-|   |-|   |-|   |-|   |-|   |-|   |-|   |-|   |-|O O|
#        └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └---┘ └-ˇ-┘
#         └ └   └ └   └ └   └ └   └ └   └ └   └ └   └ └   └ └   └ └   └ └
"""Řešení viz soubor stonozka.py"""
