import turtle as t
import random as r

t.shape("turtle")
t.bgcolor("black")
t.color("white")
t.speed(100)

penColour = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    ]

def BoundaryCheck():
    if t.ycor() >= 400:
        t.up()
        t.goto(t.xcor(), 390)
        t.down()
        print("y tp")
    elif t.ycor() <= -400:
        t.up()
        t.goto(t.xcor(), -390)
        t.down()
        print("y tp")
    if t.xcor() >= 850:
        t.up()
        t.goto(800, t.ycor())
        t.down()
        print("x tp")
    elif t.xcor() <= -850:
        t.up()
        t.goto(-800, t.ycor())
        t.down()
        print("x tp")

while True:
    BoundaryCheck()
    t.pencolor(penColour[r.randint(0, 6)])
    if r.randint(0, 1) == 0:
        t.left(r.randint(90, 170))              
    else:
        t.right(r.randint(90, 170))
    t.forward(r.randint(1, 200))



