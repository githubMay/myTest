import turtle
def drawFiveStar(t,b):
    """画五角星函数，t是画板的形式参数，b是五角星的边长"""
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


def drawPentagram(m,angle,l,a):
  
    #angle是所画五角形起点与大五角形中心连线与x轴的夹角，l是起点与大五角形中心的距离，a是所画五角形起点与此五角形中心的距离
    m.penup()
    m.goto(50,-50)
    m.left(angle)
    m.forward(l*10) 
    if a==3:
        b=2.1;angle1=162#angle1是画笔画大五角形，到达第一个起点后偏转的角度，偏转后画第一笔
    else:
        b=1.19;angle1=-18#画其他小五角的偏转的角度
    print(b,angle1,angle)
    m.right(angle1)
    drawFiveStar(m,b*10)
    m.setheading(0)
