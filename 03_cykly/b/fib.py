n = int(input("Zadejete pocet Fibonacciho cisel, ktera chce vypsat> "))


Fnp = 0  # predposledni cislo
Fn = 1  # posledni cislo
print(Fnp, Fn)  # prvni dve cisla zname
for i in range(n-1):
    tmp = Fn  # schovame si posledni cislo
    Fn = tmp + Fnp  # nove cislo je posledni plus predposledni
    Fnp = tmp  # posledni cislo je ted nove predposledni
               # a stare predposledni muzeme zapomenout
    print(Fn)  # vytiskneme
