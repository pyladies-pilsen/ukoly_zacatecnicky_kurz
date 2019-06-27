
# 03 - ZMENY V SEZNAMECH
# Seznamy jsou MENITELNE (MUTABLE), takze se do nich daji pridat prvky, daji se z nich smazat prvky a take se prvky daji menit
# Je to dulezitejsi vlastnost, nez by se mohlo zdat!

# PRIDAVANI PRVKU - lze nekolika zpusoby
# operator + spoji dva seznamy
seznam_obci = ['Misov','Cicov','Borovno']
#seznam_obci = seznam_obci +['Planiny', 'Padrte']
#print(seznam_obci)

# metoda append() prida polozku na konec seznamu

def pridej_obce(seznam):
    seznam.append('Kolvin')
    print(seznam)

#pridej_obce(seznam_obci)

# UKOL 03: Pridej dalsi obce, nemusis ve funkci



# Nemusime pridavat vzdy jen jeden prvek, muze se stat, ze jich potrebujeme pridat vic
# a k tomu slouzi funkce extend

# Pridame par dalsich obci
def pridej_vic_obci(seznam):
    seznam.extend('Prikosice','Skorice')
    print(seznam)

#pridej_vic_obci(seznam_obci)

# Vzdyt to nefunguje?
# Nefunguje to proto, ze funkce extend bere jen 1 argument, ale ted si mysli, ze ji predavame 2.
# Pokud ji chceme predat list, musime ji to dat vedet pomoci hranatych zavorek []

def pridej_vic_obci_spravne(seznam):
    seznam.extend(['Trokavec','Visky'])
    print(seznam)

#pridej_vic_obci_spravne(seznam_obci)

#Metoda extend umí pracovat i s jinými typy než se seznamy – ráda zpracuje cokoli, přes co umí cyklit for: např. jednotlivé znaky řetězců, řádky souborů, nebo čísla z range().
#seznam_obci.extend(range(2))
#seznam_obci.extend('abcdef')
#print(seznam_obci)

#a jeste bychom chteli vkladat treba doprostred,
#metoda insert() nam pomuze, ma dva argumenty,
#index polozky, ktera bude odsunuta a hodnotu, kterou chcem vlozit

#seznam_obci.insert(2,'Visky')
#print(seznam_obci)

# A co kdyz budeme chtit ale pridat samotnej seznam do seznamu?
# Tak pouzijeme append

def pridej_seznam_do_seznamu(seznam):
    seznam.append(['Trokavec','Visky'])
    print(seznam)

#pridej_seznam_do_seznamu(seznam_obci)
