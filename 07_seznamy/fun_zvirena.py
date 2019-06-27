

domaci_zvirata = ["kráva", "pes", "kocka", "králík", "had", "andulka"]
domaci_zvirata2 = ["kráva", "pes", "lachtan", "králík", "had", "andulka", "tygr"]

def vytvor_seznamy(s1, s2):

    s1ms2 = []
    s2ms1 = []
    union = []
    intersection = []

    for item in s1 + s2:
        if item not in s1:
            s2ms1.append(item)
        elif item not in s2:
            s1ms2.append(item)
        elif item not in intersection:
            intersection.append(item)

        if item not in union:
            union.append(item)

    return s1ms2, s2ms1, intersection, union


def vrat_kratsi5(seznam):
    res = []
    for e in seznam:
        if len(e) < 5:
            res.append(e)
    return res


def vrat_k(seznam):
    res = []
    for e in seznam:
        if e[0].lower() == "k":
            res.append(e)
    return res


def je_v_seznamu(slovo, seznam=domaci_zvirata):
    return slovo in seznam


def serad_abecedne(seznam):
    return sorted(seznam)


def serad_special(seznam):
    klice = [item[1:] for item in seznam]
    dvojice = list(zip(klice, seznam))
    return [item[1] for item in sorted(dvojice)]


# print(vytvor_seznamy(domaci_zvirata, domaci_zvirata2))
print(serad_abecedne(domaci_zvirata))
print(serad_special(domaci_zvirata))
