# 06 - OPERACE NAD SEZNAMY

seznam_obci = ['Misov','Cicov','Borovno','Planiny']
pocet_obyvatel = [115,182,99,5]

# Se seznamy muzeme provadet spoustu operaci, ktere uz zname napriklad od retezcu.
# Muzeme zjistit na delku (pocet zaznamu v listu), muzeme je nasobit, muzeme je prochazet v cyklu,
# muzeme je i tvorit v cyklu, muzeme je rozdelit atd.

def zdvojnasob_seznam(seznam1,seznam2):
    print('seznamy se daji nasobit a secist s dalsim seznamem: {}'.format((seznam1*2)+seznam2))
#zdvojnasob_seznam(seznam_obci,pocet_obyvatel)

# delka seznamu se fakt hodi, protoze se podle ni casto muze iterovat treba v cyklu

def dej_mi_delku_seznamu(seznam):
    print('pocet prvku v seznamu je: {}'.format(len(seznam)))

#dej_mi_delku_seznamu(seznam_obci)

#muzeme zjistit i pocet prvku v seznamu a jeho pozici

def dej_mi_pocet_Cicovu_a_jejich_index(seznam):
    print('pocet Cicovu je: {} a index Cicova je: {}'.format(seznam.count('Cicov'),seznam.index('Cicov')))

#dej_mi_pocet_Cicovu_a_jejich_index(seznam_obci)

# UKOL: co se stane, kdyz bude vic stejnych polozek v seznamu?
#Jaky index nam to vrati a proc? Vyzkousejte, muzete pouzit treba takovy seznam:
seznam_obci_2 = ['Misov','Cicov','Misov']



# sikovny operator je i "in" diky kteremu muzeme treba vytvaret podminky:

def male_obce(seznam):
    if 'Planiny' in seznam:
        print('Mate v seznamu same male obce.')
    else:
        print('No ted uz tam aspon neni ta nejvetsi dira.')

#male_obce(seznam_obci)
#male_obce(seznam_obci_2)

# seznamy lze vyuzit v podminkach a cyklech, protoze prazdny seznam vraci False, neprazdny True

def je_seznam_prazdny(seznam):
    if seznam:
        print('V seznamu neco je!')
    else: print('V seznamu nic neni!')

#je_seznam_prazdny(seznam_obci)

# stejne jako pro prevod na retezce funguje funkce str() a pro prevod na cela cisla funkce int(),
# mame neco podobneho i pro listy

def udelej_mi_z_toho_list(neco_z_ceho_chceme_list):
    novy_list = list(neco_z_ceho_chceme_list)
    print('tady mas ten list: {}'.format(novy_list))

#udelej_mi_z_toho_list('Pyladies')
#udelej_mi_z_toho_list(range(20))
#udelej_mi_z_toho_list(5)

# To posledni nevyslo, je to proto, ze list muzeme udelat jen z neceho, pres co muzeme iterovat -
# z neceho, co muze projit for cyklus a rozsekat to na mensi jednotky...u samotneho jednoho cisla to nejde

def rekni_mi_kolik_obyvatel_ma_obec():
    kolik_obyvatel = []
    for obec in seznam_obci:
        pozice = seznam_obci.index(obec)
        kolik_obyvatel.append([obec,str(pocet_obyvatel[pozice])]) #udelala jsem si seznam seznamu
    print(kolik_obyvatel)

#rekni_mi_kolik_obyvatel_ma_obec()

# vzhledem k tomu, ze retezce a listy jsou si dost podobne, muzeme se k nim casto chovat podobne
# funkce SPLIT muze rozdelit retezec na slova

def vrat_mi_seznam_slov(retezec):
    return retezec.split() #lze zadat argument = oddelovac (',' ';'  ),

slova = vrat_mi_seznam_slov('Je to asi trosku divny, ale z retezce se proste da udelat seznam znaku celkem jednoduse.')
#print(slova)

def spoj_zase_vetu(slova):
    print(' '.join(slova))

#spoj_zase_vetu(slova)

# seznamy se daji dobre michat i s random funkcemi, tzn. kdyz uz mame seznam vic hodnot, muzeme je nahodne zprehazet
# nebo z nich muzeme vybirat nahodne prvky
# musime si ale naimportovat modul random

import random

def vypisuj_nahodne(seznam):
    for i in range(10):
        print(random.choice(seznam))

#vypisuj_nahodne(seznam_obci)

def zprehazej_seznam(seznam):
    random.shuffle(seznam)
    print(seznam)

#zprehazej_seznam(seznam_obci)

# Aby toho nebylo malo, seznamy muzou obsahovat dalsi seznamy
# a neni to zadna velka veda, pracuje se s nimi stale celkem normalne
# pristupujeme k hodnotam pres indexy, iterujeme pres for cyklus,...

# rekneme, ze male obce jsou prvni podseznam, stredni obce ten druhy a velke jsou posledni

obce_podle_velikosti = [['Misov', 'Planiny'],['Porici','Rokycany'],['Plzen','Praha']]

def vypis_mi_male_obce(seznam):
    print(seznam[0])
#vypis_mi_male_obce(obce_podle_velikosti)

def vypis_mi_prvni_velkou_obec(seznam):
    velke = seznam[2]
    print(velke[0])
    print(seznam[2][0])

#vypis_mi_prvni_velkou_obec(obce_podle_velikosti)


# UKOL - Dopln kod, aby se vypsala tabulka plna cisel nasobilky
# Napr.: 3. sloupec a 5. radek obsahuje cislo 15

def vytvor_tabulku(velikost=11):
    #: vytvor pole radku
    radky=[]

        #: vytvor radek (pole cisel)


            #: pridej do radku (nezapomen, ze radek je seznam cisel) hodnotu (radek * sloupec)


        #: pridej radek do pole radku

    #: vrat pole radku
    return radky


#nasobilka = vytvor_tabulku()

# Vypsání celé tabulky
#for radek in nasobilka:
#        for cislo in radek:





#TODO: vypis hodnotu 2*3 z nasobilky

#TODO: vypis hodnotu 4*5 z nasobilky
