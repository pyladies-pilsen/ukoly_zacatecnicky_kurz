"""
Obsahuje tridu bicykl pro simulaci jizdnihoa kola
"""


class Bicykl:

    def __init__(self, barva="cerna", prevody=4):
        self.barva = barva
        self.prevody = prevody
        self.rychlost = 0
        self.prevod = 1

    def zvys_prevod(self):
        if self.prevod < self.prevody:
            self.prevod += 1
            return True
        else:
            print("Vic prevodu uz nemam")
            return False

    def sniz_prevod(self):
        if self.prevod > 1:
            self.prevod -= 1
            return True
        else:
            print("Zpatecku nemam")
            return False

    def prerad(self, novy_prevod):
        if (0 < novy_prevod) and (novy_prevod <= self.prevody):
            self.prevod = novy_prevod
            return True
        else:
            print("Takovy prevod nejde zaradit")
            return False


    def slapni(self):
        self.rychlost += self.prevod

    def brzdi(self):
        if self.rychlost > 0:
            self.rychlost -= 1
        else:
            print("Stojim")

    def zastav(self):
        while self.rychlost >= 0:
            self.brzdi()
