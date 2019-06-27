from math import sqrt
from turtle import forward, left, right, done, pendown, penup

strana = 20
populace = 5
for i in range(populace):
    # nakreslime domecek
    forward(strana)
    left(90)
    forward(strana)
    left(90)
    forward(strana)
    left(90)
    forward(strana)
    left(90)
    left(45)
    forward(sqrt(2) * strana)
    left(90)
    forward(sqrt(2) * strana / 2)
    left(90)
    forward(sqrt(2) * strana / 2)
    left(90)
    forward(sqrt(2) * strana)

    # a posuneme se k sousedovi
    left(45)  # nejdriv se musime srovnat, aby byla ulice rovne
    forward(10)


done()
