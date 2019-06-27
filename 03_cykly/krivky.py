"""
Nakreslí kochovu křivku
a část serpinského trojúlehníka
"""


import turtle as t


def koch_rek(i, length):
    if i < 1:
        t.forward(length)
        return
    else:
        koch_rek(i - 1, length / 3)
        t.left(60)
        koch_rek(i - 1, length / 3)
        t.right(120)
        koch_rek(i - 1, length / 3)
        t.left(60)
        koch_rek(i - 1, length / 3)


def serp(n, delka):

    serp_rek(n, delka)


def serp_rek(i, delka):
    t.up()
    t.fd(delka / 2)
    t.down()
    t.right(60)
    # if i > 0:
    #     serp_rek(i-1, delka/2)
    t.fd(delka / 2)
    t.right(120)
    t.fd(delka / 2)
    t.right(120)
    t.fd(delka / 2)
    t.right(120)
    if i > 0:
        serp_rek(i-1, delka/2)

def koch_line(i, delka):
    t.up()
    t.setx(-t.window_width()/2 + 20)
    t.down()
    koch_rek(i, delka)


def koch_flake(i, delka):
    t.up()
    t.setx(-t.window_width() * 4/5 / 2)
    t.sety(t.window_height() / 4)
    t.down()

    koch_rek(i, delka)
    t.right(120)
    koch_rek(i, delka)
    t.right(120)
    koch_rek(i, delka)


if __name__ == '__main__':
    t.speed(0)
    t.shape("turtle")
    # for i in range(5):
    #     koch_flake(i, t.window_width() * 4/5)
    #     t.right(120)
    koch_flake(5, t.window_width() * 4 / 5)
    t.right(120)
    serp(5, t.window_width() * 4/5)
    # koch_flake(4, 300)
    t.hideturtle()
    t.done()


