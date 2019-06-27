zaznamy = ['pepa novak', 'Jiri Sladek', 'Ivo navratil', 'jan Polednik']

# oprav zaznamy tak, aby kazde jmeno i prijmeni zacinalo velkym pismenem
# funkce, ktera prevadi prvni pismeno na velke je retezec.capitalize(), funkce nic nevraci
# funkce, ktera overi, jestli je pismenko male je retezec[index_pismenka].islower()
# -> vraci True, pokud je male a False, pokud je velke
# pro opravu zaznamu nepotrebujes prvni dve funkce (vyber_chybne_zaznamy ani vyber_spravne_zaznamy),
#  takze klidne vypracuj jen tu hlavni, treti, funkci, pokud vis rovnou, jak na to :)
# urcite budes potrebovat for cyklus, abys proiterovala cely seznam "zaznamy"


def vyber_chybne_zaznamy(zaznamy):
    pass

#print(vyber_chybne_zaznamy(zaznamy))

def vyber_spravne_zaznamy(zaznamy):
    pass

#print(vyber_spravne_zaznamy(zaznamy))

def oprav_zaznamy(zaznamy):
    for index,jmeno in enumerate(zaznamy):
        if jmeno[0].islower():
            opr_jmeno=jmeno.capitalize()
            print(opr_jmeno)

        if jmeno[jmeno.index(' ')+1].islower():
            opr_jmeno[jmeno.index(' ')+1:]=opr_jmeno[jmeno.index(' ')+1:].upper
        zaznamy[index]=opr_jmeno
    return zaznamy
print(oprav_zaznamy(zaznamy))
