## SEZNAMY - LISTS ##

# 01 - INICIALIZACE



# Prazdny seznam
seznam = []
#print(seznam)


# Seznam obsahujici nejake hodnoty

seznam_obci = ['Misov','Cicov','Borovno','Planiny']
#print(seznam_obci)


#seznam muzeme prochazet po jednotlivych prvcich

def vypis_obci(list_obci):
    for obec in list_obci:
        print(obec)

#vypis_obci(seznam_obci)

# UKOL 01: Vytvor seznam něčeho, co máš rád/a a vytiskni seznam (a zkus do jedne radky)





# Seznamy muzou obsahovat ruzne datove typy, je to heterogenni datova struktura

def vytvor_typove_nesourody_seznam(polozka):
    typove_nesourody_seznam = ['Je', True, 'ze', 'je', 'dnes', polozka, ['. rijna', 2018,'?'],None]
    return typove_nesourody_seznam

#print(vytvor_typove_nesourody_seznam(30))
