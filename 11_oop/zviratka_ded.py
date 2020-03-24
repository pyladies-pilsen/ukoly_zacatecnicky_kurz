"""
Inheritance examples from materials
https://naucse.python.cz/course/pyladies/beginners/inheritance/
"""

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Morcatko(Zviratko):
    pass

lucinka = Morcatko("Lucinka")
lucinka.snez("mrkev")


class Kotatko(Zviratko):
    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))


class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))


micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('myš')
azorek.snez('kost')