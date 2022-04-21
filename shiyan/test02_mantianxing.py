import turtle as t
import random

t.pensize(1)
t.delay(1)
t.hideturtle()
t.screensize(800,800,'black')

def starts(x,y,left_angle,edge_len):
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    t.left(left_angle)
    for _ in range(5):
        t.forward(edge_len)
        t.right(144)
    t.end_fill()
    t.left(-left_angle)

for _ in range(300):
    x=random.randint(-450,450)
    y=random.randint(0,400)
    edge_len=random.randint(3,8)
    left_angle=random.randint(0,180)
    starts(x,y,left_angle,edge_len)
t.exitonclick()