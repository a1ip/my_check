from turtle import Turtle

t = Turtle()
def Spirala(side):
    if side == 0: return 0
    global t
    t.goto(0,side)
    t.goto(side, 0)
    return Spirala()


Spirala(10)
