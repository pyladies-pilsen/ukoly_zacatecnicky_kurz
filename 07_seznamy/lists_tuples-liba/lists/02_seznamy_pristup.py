
# 02 - PRISTUP K HODNOTAM V SEZNAMU

# Seznamy jsou SERAZENE a kazda hodnota ma svuj INDEX, ktery urcuje misto (poradi), na kterem se hodnota nachazi.
# Indexy (poradi) nezacinaji od 1, nybrz od 0, je to stejne jako u retezcu!

# Vypiseme si prvni obec ze seznamu obci
seznam_obci = ['Misov','Cicov','Borovno','Planiny']
#print(seznam_obci[0])

# UKOL 02: Vypis druhou obci a pak i tu treti


# Nekdy muzeme chtit zjistit, co je na prvnich nekolika mistech v seznamu,
# nebo treba prave na tech poslednich mistech.
# To nam Python umi ukazat pomoci SLICE funkce.

# Ted si vypiseme vsechny obce od 3. v poradi:
#print(seznam_obci[2:])

# Takto si zase vypiseme vsechny obce od zacatku az do tretiho.
#print(seznam_obci[:2])

# Je to spravne? Neni.
# Slice je exclusive - nefunguje jako "vcetne", takze pokud chceme vsechny az po treti obec VCETNE, musime pridat +1
#print(seznam_obci[:3])

#Obecne plati pekna symetrie, seznam_obci[:n] je prvnich n polozek, seznam_obci[n:] vrati zbytek SEZNAMU
#[:] vsechny polozky seznamu
#Vyzkousejte pro ruzne n


# Dokonce muzeme zjistit i pozici, na ktere se konkretni hodnota (obec) nachazi

#print('Borovno se nachazi na indexu:{}'.format(seznam_obci.index('Borovno')))

# Obcas muzeme potrebovat pristupovat k hodnote i indexu soucasne, i to nam Python umoznuje

def dej_mi_pozici_i_hodnotu(seznam):
    for pozice, hodnota in seznam:
        print(pozice, hodnota)

#dej_mi_pozici_i_hodnotu(seznam_obci)

# Chybka???
# Bohuzel se k indexu a hodnote zaroven neda dostat tak uplne jednoduse, musime si zavolat na pomoc pythoni funkci 'enumerate'

def dej_mi_pozici_i_hodnotu_spravne(seznam):
    for pozice, hodnota in enumerate(seznam):
        print(pozice, hodnota)

#dej_mi_pozici_i_hodnotu_spravne(seznam_obci)
