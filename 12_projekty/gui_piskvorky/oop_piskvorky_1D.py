"""
Hra 1D piškvorky použitá při výuce PyLadies Plzeň, OOP provedení připravené
pro použití jako součást dalších programů.
"""
from random import randrange


class Hra_piskvorek1D():

    zpravy = {"x": "Vyhrál x.",
              "o": "Vyhrál o.",
              "!": "Remíza",
              "-": "Hrajeme dál"}

    def __init__(self, rozmer=10):
        """
        :param rozmer: pocet znaku v hernim poli
        """
        self.nova_hra(rozmer)

    def nova_hra(self, rozmer):
        """
        Umožňuje resetovat hru s novým herním polem o daném rozměru
        :param rozmer: pocet znaku v hernim poli
        """
        self.herni_pole = rozmer * "-"
        self.rozmer = rozmer

    def vyhodnot(self):
        """
        :return: "x" při výhře x,
                 "o" při výhře o
                 "!" při remíze
                 "-" při otevřené hře
        """
        if "xxx" in self.herni_pole:
            return "x"
        elif "ooo" in self.herni_pole:
            return "o"
        elif not ("-" in self.herni_pole):
            return "!"
        else:
            return "-"

    def _tahni(self, cislo_policka, symbol):
        self.herni_pole = \
                         self.herni_pole[0:cislo_policka] + \
                         symbol + \
                         self.herni_pole[cislo_policka+1:]

    def tah_pocitace(self):
        """
        Vygeneruje náhodný tah počítače, vrací pozici, na kterou počítač táhl.
        :return:
        """
        if "-" not in self.herni_pole:
            raise ValueError("Pole je plné, již není kam táhnout")
        while True:
            pozice = int(randrange(0, len(self.herni_pole)))
            if self.herni_pole[pozice] == "-":
                self._tahni(pozice, "o")
                return pozice

    def tah_hrace(self, cislo_policka):
        """
        Zpracuje tah hráče, vrací zprávu, pokud je tah neplatný
        :param cislo_policka: cislo herniho pole od 0 do self.rozmer-1
        :return: None pokud je tah platný, string pokud ne
        """
        if "-" not in self.herni_pole:
            raise ValueError("Pole je plné, již není kam táhnout")
        pozice = cislo_policka
        if (0 <= pozice) and (pozice < self.rozmer):
            if self.herni_pole[pozice] == "-":
                self._tahni(pozice, 'x')
                return None
            else:
                return "Pozice je obsazena"
        else:
            return "Hrajte jen v herním poli tj. od 1 do {}".format(self.rozmer)


# main aby nezačala hra při importu
if __name__ == '__main__':
    hra = Hra_piskvorek1D(20)
    while True:
        cislo_tah_hrace = int(input("Zadejte pozici v rozsahu 1 - {}: ".format(hra.rozmer)))

        chyba = hra.tah_hrace(cislo_tah_hrace - 1)

        if chyba is not None:
            print(chyba)
            continue
        print(hra.herni_pole)
        if hra.vyhodnot() != "-":
            break
        hra.tah_pocitace()

        print(hra.herni_pole)

        if hra.vyhodnot() != "-":
            break

    if hra.vyhodnot() == "!":
        print("Remíza, nikdo nevyhrál.")
    elif hra.vyhodnot() == "x":
        print("Gratuluji vyhráli jste.")
    else:
        print("Ted jsem vyhrál já.")
