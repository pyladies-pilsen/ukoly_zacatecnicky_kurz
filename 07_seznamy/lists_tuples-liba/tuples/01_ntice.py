# 01 - TUPLES (N-TICE)

# Jsou to datove struktury obsahujici obvykle vice prvku
# Nejsou uplne stejne jako seznamy

# Narozdil od seznamu jsou NEMENITELNE -> neda se k nim pridavat, neda se z nich mazat a nedaji se jim menit hodnoty
# Ale stejne jako seznamy jsou SERAZENE

# Tuple vypada treba takto:
ntice_obci = 'Misov','Cicov','Borovno'
ntice_pocet_obyvatel = 115, 182, 99, 5

# Nepouzivaji zadne hranate [], slozene {} nebo jine zavorky, proste se hodnoty jen oddeli carkou
#Ale bacha, kdyz predavame tuple jako argument nejake funkce!

def vypis_obce(ntice):
    for obec in ntice:
        print(obec)

#vypis_obce('Misov','Cicov','Borovno')

# Ajaj, Funkce potrebuje nejak vedet, co jsou jednotlive argumenty a co uz jsou hodnoty, ktere se ji snazime predat
#vypis_obce(ntice_obci)
#vypis_obce(('Misov','Cicov','Borovno'))

def rekni_mi_kolik_obyvatel(obec):
    pozice = ntice_obci.index(obec)
    obyvatel = ntice_pocet_obyvatel[pozice]
    return obec, obyvatel

#print(rekni_mi_kolik_obyvatel('Cicov'))
#obec_x, obyvatel_x = rekni_mi_kolik_obyvatel('Misov')
#print('{} ma {} obyvatel'.format(obec_x, obyvatel_x))

# Hodnoty z dvou tuplu se daji kombinovat mnohem elegantneji a sice pouzitim funkce zip()
# funkce zip funguje podobne jako zip na mikine, takze spoji hodnoty z obou ntic na stejne pozici

def rekni_mi_kolik_obyvatel_zip(obce,ntice_pocet_ob):
    for obec, lidi in zip(obce,ntice_pocet_ob):
        print('{} má {} obyvatel'.format(obec, lidi))

#rekni_mi_kolik_obyvatel_zip(ntice_obci,ntice_pocet_obyvatel)

# Enumerate proiteruje list nebo i tuple s jeho indexy i hodnotami
def vypis_index_kazde_obce(ntice):
    for index,obec in enumerate(ntice):
       print('na indexu {} je obec {}'.format(index, obec))

#vypis_index_kazde_obce(ntice_obci)

#Opet i Ntice lze pouzit v podmince Prazdna - False, Neprazdna -True
#Zkuste napsat podminku nebo while cyklus s pomoci ntice


# funkce list() a tuple () muzeme pouzit pro prevod mezi jednotlivymi datovymi strukturami
#Vyzkousejte si tyto funkce:



#Zajimavost - prirazeni vice hodnot najednou
v = ('ah', True, 'a')
#print (v)
(x, y, z) = v

#print(x)
#print(y)
#print(z)
