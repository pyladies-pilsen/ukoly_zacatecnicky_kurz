import turtle as t

strana = 50
# hexagon
for i in range(6):
    t.right(60)
    t.forward(strana)
    for j in range(6):
        t.left(60)
        t.forward(strana)
t.done()
