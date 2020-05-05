"""
Tento modul obsahuje vyrokovou
logiku implementovanou pomocí lambda kalkulu,
funkce jsou navíc typované.
"""
from typing import Callable

fboolT = Callable[[Callable, Callable], Callable]


def TRUE(x: Callable, y: Callable) -> Callable:
    return x


def FALSE(x: Callable, y: Callable) -> Callable:
    return y


def NOT(x: fboolT) -> fboolT:
    return x(FALSE, TRUE)


def AND(x: fboolT, y: fboolT) -> fboolT:
    return x(y, FALSE)


def OR(x: fboolT, y: fboolT) -> fboolT:
    return x(TRUE, y)

