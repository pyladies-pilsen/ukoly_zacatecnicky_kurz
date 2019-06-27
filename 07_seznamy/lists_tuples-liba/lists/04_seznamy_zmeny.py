
# 04 - ZMENY V SEZNAMECH

# ZMENY PRVKU
# Prvky seznamu se daji modifikovat, takze muzeme zmenit jakoukoli hodnotu v seznamu.

seznam_obci = ['Misov','Cicov','Borovno','Planiny']
#print(seznam_obci)

def zmen_Borovno_za_Skorice(seznam):
    seznam[2] = 'Skorice'
    print('tohle je jiny seznam misto Borovna jsou Skorice: {}'.format(seznam))

#zmen_Borovno_za_Skorice(seznam_obci)

# UKOL 04: Zmen nekterou obec za jinou, nemusis nutne pres funkci :)




# A nam se vlastne nelibi ani ten Cicov, dejme ho pryc.
# prikaz del smaze hodnotu z daneho indexu, nebo klidne i vic hodnot, pokud zadame rozsah jako [2:4]

def zrus_Cicov(seznam):
    del seznam[1]
    print('tohle je seznam bez Cicova: {}'.format(seznam))

#zrus_Cicov(seznam_obci)

# metoda pop() vyhodi a vrátí posledni prvek ze seznamu, pokud zadáme index vyhodi a vrati vybrany prvek
# Volanim metody pop() nad prazdnym seznamem vznikne vyjimka

def zrus_posledni(seznam):
    vypusteny=seznam.pop()
    print('tohle je uz dost vyprazdnenej seznam: {}, vypustili jsme {}'.format(seznam,vypusteny))

#zrus_posledni(seznam_obci)

# A taky Misov pryc
# pri pouziti metody remove() pro neexistujici polozku seznamu - bude opet vyvolana vyjimka

def prvek_pryc(seznam):
    seznam.remove('Misov')
    print('uz tu je toho malo: {}'.format(seznam))
#prvek_pryc(seznam_obci)

# No a vycistime cely seznam

def vycisti_seznam(seznam):
    seznam.clear()
    print('a tady pojedem odznova s prazdnou: {}'.format(seznam))
#vycisti_seznam(seznam_obci)
