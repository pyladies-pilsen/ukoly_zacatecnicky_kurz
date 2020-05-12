

def rim2arb(rim_cislo):

    prevody = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500 ,"m": 1000}
    arb_cislo = 0
    rad = 0
    for rc in rim_cislo.lower()[::-1]:
        ac = prevody[rc]
        if ac >= rad:
            arb_cislo += ac
            rad = ac
        else:
            arb_cislo -= ac

    return arb_cislo

print(rim2arb("MCMXXCIV"))