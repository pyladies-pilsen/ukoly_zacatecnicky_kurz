bin_cislo = input("Zadejte číslo v binární soustavě: ")

dec_cislo = 0

bin_cislo_z = bin_cislo[::-1]
mocnina = 1

for c in bin_cislo:
    dec_cislo = dec_cislo + int(c) * mocnina
    mocnina = mocnina * 2

print(dec_cislo)