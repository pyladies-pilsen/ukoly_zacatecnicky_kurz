print("Zadávejte čísla.")
pocet = 0
for i in range(5):
    cislo = float(input("Zadej číslo: "))
    if cislo > 42:
        pocet += 1

print(pocet)
