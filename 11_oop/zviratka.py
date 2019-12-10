"""
Inheritance examples from materials
https://naucse.python.cz/course/pyladies/beginners/inheritance/
"""


class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))

    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))


class Stenatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))

    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))
