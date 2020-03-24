"""
Tento script obsahuje reseni nekterych ukolu na cykly
ve stylu funcionalniho programovani
"""

from toolz import *
from operator import mul, and_, add
from math import sqrt, ceil


print("".join(map(lambda x: "a\n", range(5))))

print("".join(map(lambda x: "Radek {0}\n".format(x), range(5))))

print("".join(map(lambda x: "{0} na druhou je {1}\n".format(x, x**2), range(5))))

print("".join(map(lambda y: "".join(map(lambda x: "x", range(5))) + "\n", range(5))))

print("".join(map(lambda y: "".join(map(lambda x: " {0}".format(y*x), range(5))) + "\n", range(5))))

print(list(map(lambda y: list(map(lambda x: " {0}".format(y*x), range(5))), range(5))))

print(list(map(list, map(lambda y: map(lambda x: " {0}".format(y*x), range(5)), range(5)))))

print("\n".join(map("".join, map(lambda y: map(lambda x: " {0}".format(y*x), range(5)), range(5)))))

print("".join(map(lambda y: "".join(map(lambda x: "x", range(y))) + "\n", range(1, 5))))

print(reduce(mul, range(1, int(input("Zadejte cislo: "))+1)))


def is_prime(N):
    if N == 2:
        return True
    elif N == 1:
        return False
    return reduce(and_, map(lambda x: N % x != 0,
                            cons(2, range(3, int(ceil(sqrt(N))+1), 2))))


# print(is_prime(int(input("Zadejte N: "))))

ispf = (lambda N: N == 2 if N < 3 else reduce(and_,
                                             map(lambda x: N % x != 0,
                                                 cons(2, range(3, int(ceil(sqrt(N))+1), 2)))))


def fib(N):
    f = iterate(
        lambda x: list(cons(first(x) + second(x), x)),
        [1, 1])
    return list(map(lambda x: next(f), range(N)))[-1][::-1]


def fibt(N, N_1=1, N_2=1):
    if N == 0:
        return N_1
    else:
        return fibt(N - 1, N_2, N_1 + N_2)


fibf = partial(lambda f, N: list(map(lambda _: next(f), range(N-1)))[-1][::-1],
               iterate(lambda x: list(cons(first(x) + second(x), x)), [1, 1]))

fibfp = partial(flip(nth, iterate(lambda x: list(cons(first(x) + second(x), x)), [1, 1])))

fibfn = (lambda N: list(reversed(nth(N, iterate(lambda l: list(cons(first(l) + second(l), l)), [1, 1])))))

# infinite loop
# list(map(print, iterate(lambda x: list(cons(first(x) + second(x), x)), [1, 1])))

zvirata = ["pes", "kocka", "králík", "had"]
len5 = (lambda l: list((filter(lambda z: len(z) < 5, l))))
startk = (lambda l: list((filter(lambda z: z[0] == 'k', l))))
isnz = (lambda s: s in zvirata)

# print(isnz("ptakopysk"))

# quine, is there easier way?
# print("{0}.format(r\'{0}\'))".format(r'print("{0}.format(r\'{0}\'))"'))

seznam = nth(18, iterate(lambda l: list(range(5)) + [l], [5]))
seznam = [5, 3, 3, 3, 3]
seznam.append(seznam)
print(seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0] == 5)

pole = list(map(lambda y: list(map(lambda x: ".", range(10))), range(10)))


def pol_print(pole):
    print("\n".join(map("".join, pole)))


def place(pole, coors ,mark="X"):
    npole = pole.copy()
    for coor in coors:
        npole[coor[0]][coor[1]] = mark
    return npole


pol_print(place(pole, [(0, 0), (0, 1), (5, 5)]))
