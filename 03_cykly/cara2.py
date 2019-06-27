import turtle as t

krok = 1
for i in range(20):
    t.pendown()
    t.forward(krok * i)
    t.penup()
    t.forward(krok * 3)
t.done()