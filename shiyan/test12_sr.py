import turtle
import random
import time

turtle.pensize(1)
turtle.delay(1)
turtle.hideturtle()
turtle.setup(650, 400)


def star(x, y, left_angle, edge_len, color='yellow'):
    """
    画一个五角星
    :param x: 起始x坐标
    :param y: 起始y坐标
    :param left_angle: 画笔方向逆时针转动度数
    :param edge_len: 五角星边的长度
    :param color: 五角星颜色
    :return:
    """
    # 五角星边的颜色
    turtle.pencolor(color)
    # 五角星内部填充色
    turtle.fillcolor(color)
    # 绘制速度，0代表最快，1-10：数字越大越快
    turtle.speed(0)

    turtle.pu()  # 抬起画笔
    turtle.goto(x, y)  # 移动到初始位置
    turtle.pd()  # 放下画笔

    turtle.begin_fill()  # 开始填充图形
    # 画笔方向以水平方向为基准
    # 逆时针转动 left_angle 度
    turtle.left(left_angle)
    # 循环绘制五角星的 5 条边
    for _ in range(5):
        # 向画笔方向移动edge_len像素长度
        # 即：绘制五角星的一条边
        turtle.forward(edge_len)
        # 画笔方向顺时针旋转144度
        # 由于五角星内角是36度，因此旋转180-36=144度
        turtle.right(144)
    turtle.end_fill()  # 填充完成
    # 将画笔方向恢复为水平方向，以免影响后续画图
    turtle.left(-left_angle)


# 绘制满天星
# 添加背景图，需要是gif格式
turtle.bgpic('./star.gif')

tommy = turtle.Turtle()
tommy.shape('turtle')
tommy.speed(75)

# 画线
tommy.penup()
tommy.goto(-190, -180)
tommy.color('yellow')
tommy.pensize(6)
tommy.pendown()
tommy.goto(-190, -180)
tommy.penup()

tommy.penup()
tommy.goto(-130, -120)
tommy.color('teal')
tommy.pensize(6)
tommy.pendown()
tommy.goto(130, -120)
tommy.penup()

# 画蛋糕
tommy.goto(-74, -110)
tommy.pendown()
tommy.color('white')
tommy.goto(50, -110)
tommy.left(90)
tommy.forward(60)
tommy.left(90)
tommy.forward(125)
tommy.left(90)
tommy.forward(60)
tommy.penup()

# 画蜡烛
tommy.goto(-60, -40)
tommy.color('aquamarine')
tommy.pendown()
tommy.pensize(3)
tommy.goto(-60, -20)
tommy.penup()

tommy.goto(-40, -40)
tommy.color('yellow')
tommy.pendown()
tommy.pensize(3)
tommy.goto(-40, -20)
tommy.penup()

tommy.goto(-20, -40)
tommy.color('green')
tommy.pendown()
tommy.pensize(3)
tommy.goto(-20, -20)
tommy.penup()

tommy.goto(0, -40)
tommy.color('pink')
tommy.pendown()
tommy.pensize(3)
tommy.goto(0, -20)
tommy.penup()

tommy.goto(20, -40)
tommy.color('blue')
tommy.pendown()
tommy.pensize(3)
tommy.goto(20, -20)
tommy.penup()

tommy.goto(40, -40)
tommy.color('aquamarine')
tommy.pendown()
tommy.pensize(3)
tommy.goto(40, -20)
tommy.penup()

# 写字
tommy.goto(-110, 35)
tommy.color('yellow')
tommy.pendown()
tommy.write(str('Happy Birthday!'), font='60pt')
# tommy.write(str('To Tcl'),align='right',font='60pt')

'''
def Tree(branch,t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

 # 掉落的花瓣
def Petal(m,t):
     for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

w=turtle.Screen()
t=turtle.Turtle()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')  # wheat小麦
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')
# 画樱花的躯干
Tree(60, t)
# 掉落的花瓣
Petal(200, t)
w.exitonclick()
'''
# 绘制 200 颗星星
for _ in range(200):
    # 随机生成起始坐标、画笔方向和五角星边长
    rand_x = random.randint(-400, 400)
    rand_y = random.randint(0, 400)
    edge_len = random.randint(3, 8)
    left_angle = random.randint(0, 180)
    star(rand_x, rand_y, left_angle, edge_len, '#B7C5D2')

# 让画布停留
turtle.done()
