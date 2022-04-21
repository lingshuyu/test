# 生日快乐
import turtle
import random

#  设置背景颜色
bg=turtle.Screen()
bg.bgcolor('light blue')
turtle.bgpic(r'./star.gif')

tommy=turtle.Turtle()
tommy.shape('turtle')
tommy.speed(75)

#画线
tommy.penup()
tommy.goto(-190,-180)
tommy.color('yellow')
tommy.pensize(6)
tommy.pendown()
tommy.goto(-190,-180)
tommy.penup()

tommy.penup()
tommy.goto(-130,-120)
tommy.color('teal')
tommy.pensize(6)
tommy.pendown()
tommy.goto(130,-120)
tommy.penup()

#画蛋糕
tommy.goto(-74,-110)
tommy.pendown()
tommy.color('white')
tommy.goto(50,-110)
tommy.left(90)
tommy.forward(60)
tommy.left(90)
tommy.forward(125)
tommy.left(90)
tommy.forward(60)
tommy.penup()

#画蜡烛
tommy.goto(-60,-40)
tommy.color('aquamarine')
tommy.pendown()
tommy.pensize(3)
tommy.goto(-60,-20)
tommy.penup()

tommy.goto(-40,-40)
tommy.color('yellow')
tommy.pendown()
tommy.pensize(3)
tommy.goto(-40,-20)
tommy.penup()

tommy.goto(-20,-40)
tommy.color('green')
tommy.pendown()
tommy.pensize(3)
tommy.goto(-20,-20)
tommy.penup()

tommy.goto(0,-40)
tommy.color('pink')
tommy.pendown()
tommy.pensize(3)
tommy.goto(0,-20)
tommy.penup()

tommy.goto(20,-40)
tommy.color('blue')
tommy.pendown()
tommy.pensize(3)
tommy.goto(20,-20)
tommy.penup()

tommy.goto(40,-40)
tommy.color('aquamarine')
tommy.pendown()
tommy.pensize(3)
tommy.goto(40,-20)
tommy.penup()

#写字
tommy.goto(-110,35)
tommy.color('yellow')
tommy.pendown()
tommy.write(str('Happy Birthday!'),font='60pt')

#设置幕布
tommy.penup()
tommy.goto(-250,250)
turtle.done()