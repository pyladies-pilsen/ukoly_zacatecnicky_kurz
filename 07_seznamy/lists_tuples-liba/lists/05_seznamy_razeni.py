# 05 - RAZENI SEZNAMU

# Seznam je usporadana kolekce polozek

seznam_obci = ['Misov','Cicov','Borovno','Planiny']
pocet_obyvatel = [115,182,99,5]

# Seznamy se radi abecedne pokud jde o retezce

# muzeme pouzit funkci sorted(seznam), ktera nam samotny seznam NESERADI, ale jen vrati SERAZENY vystup ('nove' serazene pole)
# tato funkce tedy NEMENI seznam samotny

def vypis_serazeny_seznam(seznam):
    serazene_pole = sorted(seznam)
    print('toto je serazene pole od A, ale nezmenene: {}'.format(serazene_pole))

#vypis_serazeny_seznam(seznam_obci)

#print(seznam_obci)

# pokud ale chceme seznam zmenit, aby byl uz naporad SERAZENY, muzeme pouzit metodu seznam.sort(), ktera nase stavajici pole seradi

def serad_seznam(seznam):
    seznam.sort()
    print('toto je serazene pole od A, ktere je zmeneme "naporad": {}'.format(seznam))

#serad_seznam(seznam_obci)

# muzeme i zmenit smer razeni, tedy ne A -> Z, ale Z -> A
def serad_seznam_opacne(seznam):
    seznam.sort(reverse=True)
    print('seznam serazeny od Z: {}'.format(seznam))

#serad_seznam_opacne(seznam_obci)
#print('i funkce sorted() umi radit opacne: {}'.format(sorted(seznam_obci,reverse=True)))

# to stejne muzeme udelat i s cisly v seznamu

# UKOL: seradte seznam pocet_obyvatel, pouzijte funkci, ktera puvodni seznam ZMENI na serazeny
