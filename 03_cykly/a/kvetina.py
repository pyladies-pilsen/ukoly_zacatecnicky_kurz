from turtle import forward, left, right, exitonclick
for a in range(18):
    for b in range(4):
        forward(50)
        left(90)
    left(20)
right(90)
forward(100)
for d in range(5, 55, 5):
    if d % 2 == 0:
        left(90)
        forward(d)
        left(45)
        forward(d)
        left(135)
        forward(d)
        left(45)
        forward(d)
        left(45)
        forward(d)
    else:
        right(90)
        forward(d)
        right(45)
        forward(d)
        right(135)
        forward(d)
        right(45)
        forward(d)
        right(45)
        forward(d)
    
exitonclick()
