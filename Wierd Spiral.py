import turtle as t

#wn = t.Screen()

#wn.tracer(0)

t.shape("turtle")
t.bgcolor("black")
t.color("white")
t.speed(0)

a = 4
b = 200
c = 100000

while c > 0:
    while a > 0:
        t.right(90)
        t.forward(b)
        a -= 1
        b += 0.1
        c -= 1
    t.right(1)
    a = 4

#wn.update()

#wn.mainloop()
    

