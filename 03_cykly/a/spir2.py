import turtle as t

strana = 100

t.left(90)
for i in range(100):
    t.forward(strana - i)  # zmensujeme stranu
    t.right(360/9)  # a kreslime "9-uhelnik"

t.done()
