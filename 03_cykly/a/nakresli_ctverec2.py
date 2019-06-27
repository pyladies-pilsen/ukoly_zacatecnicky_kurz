import turtle as t


strana = 50
t.shape("turtle")
for i in range(18):
    t.forward(strana)
    t.right(90)
    t.forward(strana)
    t.right(90)
    t.forward(strana)
    t.right(90)
    t.forward(strana)
    t.right(90)
    # po kazdem ctverci se pootocime
    t.left(20)
t.done()

