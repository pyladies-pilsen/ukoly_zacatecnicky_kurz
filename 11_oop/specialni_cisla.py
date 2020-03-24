"""
Rešení úkolu na dědičnost

0. Vytvoř si vlastní třídu pro celá čísla tak, aby tato nová třída měla všechny
vlastnosti a schopnosti běžných celých čísel v Pythonu (objekty bude možné
sčítat, odečítat, porovnávat atp.) a navíc měla metodu pro rozpoznání,
zda je číslo v objektu sudé nebo liché jménem je_sude(), která bude vracet True
nebo False.

1. Jako bonus je možné vlastní třídě z předchozího příkladu přepsat metodu
__repr__() tak, aby bylo v interaktivním režimu poznat, které číslo je
standardní int a které je z tebou vytvořené třídy.
"""
class Cislo(int):

    def je_sude(self):
       if self % 2 == 0:
           return True
       else:
           return False

    def __repr__(self):
        return "Cislo({})".format(self)


cislo1 = Cislo(4)
cislo2 = Cislo("3")

print(cislo1)
print(cislo1.je_sude())
print(cislo2)
print(cislo2.je_sude())
