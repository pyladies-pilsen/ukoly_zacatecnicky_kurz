import turtle as t

def nakresli_dum(strana):
    """
    Tahle funke nakresli domecek jednim tahem,
    jde to ale spousty jinych zpusobu,

    :param strana je vyska steny domku
    """
    # nejdriv ctverec
    from math import sqrt
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
    t.forward(sqrt(2) * strana)

    # strecha je taky diagonala ale kreslime z ni jen pulku
    t.left(90)
    t.forward(sqrt(2) * strana / 2)
    t.left(90)
    t.forward(sqrt(2) * strana / 2)

    # a do praveho dolniho rohu
    t.left(90)
    t.forward(sqrt(2) * strana)
    t.left(45)


def nakresli_dum2(sirka, vyska):
    """
    Nakresli dum se zadanou vyskou a sirkou
    :param sirka:
    :param vyska:
    :return:
    """

    from math import atan, tan, degrees
    from math import sqrt
    prepona = sqrt(sirka**2 + vyska**2)  # delka diagonaly a strany na střeše
    vs = vyska/sirka  # protilehlá ku přeponě
    alf = degrees(atan(vs))  # uhel se spočítá pomocí arcustangens

    # čtverec
    t.forward(sirka)
    t.left(90)
    t.forward(vyska)
    t.left(90)
    t.forward(sirka)
    t.left(90)
    t.forward(vyska)
    t.left(90)

    # diagonala z leveho dolniho rohu do praveho horniho
    t.left(alf)
    t.forward(prepona)

    # strecha je taky diagonala ale kreslime z ni jen pulku
    t.left(180 - 2*alf)
    t.forward(prepona/2)
    t.left(2*alf)
    t.forward(prepona/2)

    t.left(180 - 2 * alf)
    t.forward(prepona)
    t.left(alf) # aby želva skončila připravená kreslit další domek



if __name__ == '__main__':
    nakresli_dum2(40, 60)
    t.forward(20)
    nakresli_dum(20)
    t.forward(30)
    nakresli_dum(50)

    t.done()
