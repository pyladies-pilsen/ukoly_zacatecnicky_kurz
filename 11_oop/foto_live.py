"""
Řešení úkolu 1.3. Kód napsaný společně na lekci.
"""


class Fotoaparat:
    def __init__(self):
        self.cas = 1000
        self.clona = 1.2
        self.max_pocet_snimku = 36
        self.cislo_akt_snimku = 0
        self.film = []
        self.natazeno = False

    def natahni(self):
        if not self.natazeno and \
                self.cislo_akt_snimku < self.max_pocet_snimku:
            self.natazeno = True
            self.cislo_akt_snimku += 1

    def zmackni_spoust(self):
        if self.natazeno == True:
            print("Cvak!")
            self.film.append("Snimek {}".format(self.cislo_akt_snimku))
            self.natazeno = False
        else:
            print("Neni natazeno!")


muj_fotak = Fotoaparat()
muj_fotak.natahni()
muj_fotak.zmackni_spoust()
muj_fotak.zmackni_spoust()



