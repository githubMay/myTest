import turtle
def draw(t,b):
    #t.pendown()
    t.begin_fill()
    t.fillcolor('yellow')
    for i in range(0,5):
        t.speed(1)
        t.forward(b)
        t.left(72)
        t.forward(b)
        t.right(144)
    t.penup()
    t.end_fill()
  