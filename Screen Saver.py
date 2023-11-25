import turtle
import random

turtle.bgcolor("black")
turtle.color("white")
turtle.shape("turtle")
turtle.shapesize(10)
turtle.up()
turtle.speed(0)


def rotateturtle():
    a = random.randint(10, 80)
    b = 180 - (a + 90)
    c = random.randint(10, b)
    d = c + b
    turtle.forward(1)
    if turtle.xcor() >= 860:
        turtle.left(d)
    elif turtle.xcor() <= -860:
        turtle.left(d)
    elif turtle.ycor() >= 400:
        turtle.left(d)
    elif turtle.ycor() <= -400:
        turtle.left(d)


turtle.left(random.uniform(10, 60))
while True:
    rotateturtle()
