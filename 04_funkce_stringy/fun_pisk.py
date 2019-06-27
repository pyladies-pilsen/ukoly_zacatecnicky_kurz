"""
Hraje piskvorky
"""
from random import randrange


def vyhodnot(hra):
    """
    :param hra:
    :return: "x" při výhře x,
             "o" při výhře o
             "!" při remíze
             "-" při otevřené hře
    """
    if "xxx" in hra:
        return "x"
    elif "ooo" in hra:
        return "o"
    elif not("-" in hra):
        return "!"
    else:
        return "-"


def tahni(hra, cislo_policka, symbol):
    """
    Zapíše symbol na pozici cislo_policka v řetězci hra,
    vrátí nový řetězec
    :param hra:
    :param cislo_policka:
    :param symbol:
    :return:
    """
    return hra[0:cislo_policka] + symbol + hra[cislo_policka+1:]


def tah_hrace(hra):
    """
    Ptá se hráče na tah dokud se nepodaří,
    vrátí nové herní pole se zaznamenaným tahem "x"
    :param hra: string, současné herní pole
    :return: nové herní pole
    """
    print("Stav hry je: ")
    print(hra)
    while True:
        pozice = int(input("Jak chcete hrat? "))
        if (0 < pozice) and (pozice <= len(hra)):
            if hra[pozice -1] == "-":
                return tahni(hra, pozice - 1, "x")
            else:
                print("Obsazena pozice, hrajte jinam.")
        else:
            print("Hrajte jen v herním poli tj. od 1 do {}".
                  format(len(hra)))
            
def tah_pocitace(hra):
    """
    Náhodně táhne "o" na volné pole
    :param hra: string, současné herní pole
    :return: nové herní pole
    """
    while True:
        pozice = int(randrange(0, len(hra)))
        if hra[pozice] == "-":
            return tahni(hra, pozice, "o")

def piskvorky1d():
    hra = 20 * "-"
    while True:
        hra = tah_hrace(hra)
        if vyhodnot(hra) != "-":
            break
        hra = tah_pocitace(hra)
        if vyhodnot(hra) != "-":
            break

    if vyhodnot(hra) == "!":
        print("Remíza, nikdo nevyhrál.")
    elif vyhodnot(hra) == "x":
        print("Gratuluji vyhráli jste.")
    else:
        print("Ted jsem vyhrál já.")

# Následující řádky se provedou,
# pouze pokud je skript spuštěn přímo
if __name__ == '__main__': 
    piskvorky1d()


