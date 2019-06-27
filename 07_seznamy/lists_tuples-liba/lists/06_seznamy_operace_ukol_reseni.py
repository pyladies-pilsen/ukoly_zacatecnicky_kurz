zaznamy = ['pepa novak', 'Jiri Sladek', 'Ivo navratil', 'jan Polednik']


def vyber_chybne_zaznamy(zaznamy):
    chybne_zaznamy = []
    for zaznam in zaznamy:
        jmeno_prijmeni = zaznam.split(' ')
        jmeno = jmeno_prijmeni[0]
        prijmeni = jmeno_prijmeni[1]
        if jmeno[0].islower() or prijmeni[0].islower():
            chybne_zaznamy.append(zaznam)
    return chybne_zaznamy

print(vyber_chybne_zaznamy(zaznamy))

def vyber_spravne_zaznamy(zaznamy):
    spravne_zaznamy = []
    for zaznam in zaznamy:
        jmeno_prijmeni = zaznam.split(' ')
        jmeno = jmeno_prijmeni[0]
        prijmeni = jmeno_prijmeni[1]
        if not jmeno[0].islower() and not prijmeni[0].islower():
            spravne_zaznamy.append(zaznam)
    return spravne_zaznamy
print(vyber_spravne_zaznamy(zaznamy))

def oprav_zaznamy(zaznamy):
    opravene_zaznamy = []
    for zaznam in zaznamy:
        jmeno_prijmeni = zaznam.split(' ')
        jmeno = jmeno_prijmeni[0]
        prijmeni = jmeno_prijmeni[1]
        if jmeno[0].islower() or prijmeni[0].islower():
            opravene_zaznamy.append(jmeno_prijmeni[0].capitalize()+' '+jmeno_prijmeni[1].capitalize())
        else:
            opravene_zaznamy.append(zaznam)
    return opravene_zaznamy

print(oprav_zaznamy(zaznamy))


