zada  =  "┌---┐ "
boky  =  "|   |-"
brisko = "└---┘ "
nohy  =  " └ └  "

stonozka = ""

pocet_nohou = 100

for i in range(pocet_nohou):
    stonozka = stonozka + zada
stonozka = stonozka + zada
stonozka = stonozka + "\n"

for i in range(pocet_nohou):
    stonozka = stonozka + boky
stonozka = stonozka + "|O O|"
stonozka = stonozka + "\n"

for i in range(pocet_nohou):
    stonozka = stonozka + brisko
stonozka = stonozka + "└-ˇ-┘"
stonozka = stonozka + "\n"

for i in range(pocet_nohou):
    stonozka = stonozka + nohy
stonozka = stonozka + "\n"


stonohy_soubor = open("s_t_o_n_o_z_k_a.txt", "w", encoding="utf-8")
print(stonozka, file=stonohy_soubor)
stonohy_soubor.close()

