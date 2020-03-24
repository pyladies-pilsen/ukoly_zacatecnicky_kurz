"""
Tento modul obsahuje vyrokovou
logiku implementovanou pomocí lambda kalkulu.
"""


def TRUE(x, y):
    return x


def FALSE(x, y):
    return y


def NOT(x):
    return x(FALSE, TRUE)


def AND(x, y):
    return x(y, FALSE)


def OR(x, y):
    return x(TRUE, y)

