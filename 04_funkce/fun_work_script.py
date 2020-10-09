# -*- coding: utf-8 -*-
#  Pracovní skript k lekci Funkce

#################################
#          Základy              #
#################################
# funkce ~ metody ~ procedury ~ podprogramy


# S podprogramy už jsme se setkali, třeba:

# ┌ jméno funkce/podprogramu
# |          ┌ argument/parametr předaný podprogramu/funkci
print("Ahoj, PyLadies!")
#    |                 |
#    └závorky označují ┘
#       volání funkce
#    spuštění podprogramu

# podprogramy mohou mít vice argumentů oddělených čárkami
#          ┌ 1. argument                      ┌ 2. argument
print('Obvod čtverce se stranou 356 cm je', 4 * 356, 'cm')
#                                                      └ 3. argument

# některé podprogramy mohou mít pojmenované argumenty
#                            ┌ řetězec, kterým budou odděleny položky ve výpisu
print("Ahoj", "PyLadies!", sep="+", end=" |\n")
#                                     └ řetězec, kterým bude výpis ukončen

# Některé podprogramy argumenty nepotřebují, aby se provedli
# musíme je ale pořád zavolat/spustit == napsat závorky.
print("# volani print")
print()

# 0. cvičení
# 0.a Zavolejte print alespon se čtyřmi argumenty.

# 0.b Jak předáme funkci turtle.forward délku posunutí?
import turtle
turtle.forward


# 0.c Jaké znáte další podprogramy/funkce? Co dělají? Jak se volají?

# 0.d Co udělá následující kód, co chybí?
print


#################################
#          Vracení              #
#################################
cislo = int("10")


# ┌ návratová hodnota
vysledek = print(1 + 2)

# print nic nevrací, resp. vrací hodnotu None,
# která označuje nic/prázdný výsledek
print("# vysledek ==", vysledek)


skutecny_vysledek = 1 + 2

# `+` "vrací" součet dvou čísel
print("# skutecny_vysledek ==", skutecny_vysledek)

# ┌ návratová hodnota
delka = len("Ahoj, PyLadies!")
#         └ funkce len spočítá délku řetězce a vrátí ji
print("# delka ==", delka)

# 1. cvičení
# 1.a Vypište délku řetězce "Za čárkou se vždy píše mezera.".

# 1.b Vypište délku řetězce "Za čárkou se vždy píše mezera." aniž
# byste si ji ukládali do proměnné.

# 1.c Sečtěte délky řetězců "Za čárkou se vždy píše mezera." a
# "Importy se píšou na začátek souboru."

# 1.b Co vrací funkce turtle.forward?
vysledek_forward = turtle.forward




#################################
#         Vytváření             #
#################################

# Vlastní podprogram vytvoříme pomocí klíčového slova def

#┌ def je klíčové slovo podobně jako for nebo if
#|       ┌ jméno podprogramu
def muj_podprogram(argument1, argument2):
    ...           #   |         └ druhý argument, atd...
#    |                └ první argument
#    └ tělo podprogramu, místo teček přijde kód popisující co podprogram dělá


def muj_print(prvni_retezec, druhy_retezec):
    print(prvni_retezec, druhy_retezec, sep="+", end="|\n")

# Definice podprogramu "nic nedělá", musíme jej zavolat/spustit.

print("# volani muj_print:")
muj_print("Ahoj", "PyLadies!")

# Jako argumenty můžeme předat i proměnné.

s1 = "Ahoj"
s2 = "PyLadies!"
muj_print(s1, s2)

# Podprogramy můžou dělat všechno, co dosud programy.

def nakresli_trojuhelnik(strana):
    turtle.forward(strana)
    turtle.left(120)
    turtle.forward(strana)
    turtle.left(120)
    turtle.forward(strana)
    turtle.left(120)

nakresli_trojuhelnik(50)

# 2. Cvičení
# 2.a Napiste podprogram muj_print3, který bude umět vytisknout tři řetězce.

# 2.b Napište podprogram secti, který bude mít jako argumenty dvě čísla cislo1
# a cislo2 a vypíše jejich součet.

# 2.c Napište podprogram nakresli_ctverec, který pomocí želví grafiky nakreslí
# čtverec o straně jejíž délka bude jeho jediným argumentem.

# 2.d napište podprogram vypis_do_sloupce, který bude mít jeden argument - řetězec,
# který vypíše do sloupce.

#################################
#           Return              #
#################################

# Vypisování je fajn ale co když chceme použít výsledek
# dál v programu podobně jako len?
# Na to máme klíčové slovo return.

def secti(cislo1, cislo2):
    vysledek = cislo1 + cislo2
#      └ Uvnitř podprogramu můžeme libovolně vytvářet proměnné,
#        ty jsou zcela oddělené od ostatních proměnných mimo podprogram.
    return vysledek

vysledek_secti = secti(1, 2)

print("# vysledek_secti ==", vysledek_secti)

print("# volani secti")
print(secti(1, 2))

print("# volani secti bez print")
secti(1, 2)

# Kličové slovo return ukončí vykonávání podprogramu, vrátí se do programu,
# který podprogram zavolal/spustil a místo volání se objeví vrácená hodnota.

a = 1
b = 2
vysledek_secti = secti(a, b)
# vvvvvvv
vysledek_secti = 3

# 3. Cvičení
# 3.a Napište podprogram secti3, který bude mít jako argumenty tři čísla
# cislo1, cislo2 a cislo3, všechny tři sečte a výsledek vrátí.

# 3.b Napište podprogram obsah_obdelnika, který dostane jako argumenty dvě čísla
# a spočítá a vrátí obsah obdélníka s těmito rozměry.

# 3.c Napište podprogram, který dostane číslo - poloměr a spočte obsha kruhu
# s tímto poloměrem, obsah kruhu se spočítá jako π×r².
from math import pi



# Podprogramy mohou vykonávat složité úkoly, o kterých nechceme vědět.
# Například mohou získat přípustnou odpověd od uživatele.
def ano_nebo_ne(otazka):
    """Vrátí True nebo False podle odpovědi uživatele"""
    while True:
        odpoved = input(otazka)
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False
        print('Nerozumím! Odpověz "ano" nebo "ne".')

# Příklad použití
#       ┌ celé otravné dotazování je schované za jedinným voláním
if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')


turtle.done()