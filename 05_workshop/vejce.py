"""Děláme míchaná vajíčka"""

from random import sample, randint


def rozklepni_vejce(vejce):
    return "bílekžloutekbílek"


def zamichej_robotem(obsah_panve):
    return "".join(sample(obsah_panve, k=len(obsah_panve)))


def zamichej_vareckou(obsah_panve, intenzita_michani=4):
    for i in range(intenzita_michani):
        # print(obsah_panve)
        pozice_michnuti = randint(0, len(obsah_panve) - 1)
        obsah_panve = obsah_panve[pozice_michnuti + 1:] + \
                      obsah_panve[pozice_michnuti] + \
                      obsah_panve[:pozice_michnuti]

    return obsah_panve


karton_vajec = ["()", "()", "()", "()"]
peprenka = ["pepř"]
slanka = ["sůl"]
lahev_oleje = ["olej"]

obsah_panve = ""
obsah_panve += lahev_oleje[0]

for vajicko in karton_vajec:
    obsah_panve += rozklepni_vejce(vajicko)

obsah_panve += peprenka[0]
obsah_panve += slanka[0]

obsah_panve = zamichej_vareckou(obsah_panve, intenzita_michani=20)
print(obsah_panve)
