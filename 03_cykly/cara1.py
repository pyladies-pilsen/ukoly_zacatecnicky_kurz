import turtle as t


krok = 20
for i in range(10):
    t.pendown()
    t.forward(krok)
    t.penup()
    t.forward(krok)
t.done()