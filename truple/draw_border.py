import turtle
def drawBorder(m):
    m.pendown()
    m.begin_fill()
    m.fillcolor('red')
    
    m.forward(300)
    m.goto(300,-200)
    m.goto(0,-200)
    m.goto(0,0)
    m.penup()
    m.end_fill()