import turtle as t
from math import sqrt

strana = 50
def nakresli_dum():
    # tohle nakresli domecek jednim tahem, jde to ale spousty jinych zpusobu
    # nejdriv ctverec
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)

    # diagonala z leveho dolniho rohu do praveho horniho
    t.left(45)
    t.forward(sqrt(2)*strana)

    # strecha je taky diagonala ale kreslime z ni jen pulku
    t.left(90)
    t.forward(sqrt(2)*strana/2)
    t.left(90)
    t.forward(sqrt(2)*strana/2)

    # a do praveho dolniho rohu
    t.left(90)
    t.forward(sqrt(2)*strana)

t.done()
