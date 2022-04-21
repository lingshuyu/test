class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池中有乌龟%d只，小鱼%d条' %(self.turtle.num,self.fish.num))

pool=Pool(1,10)
pool.print_num()
print(pool)

class C:
    def x(self):
        print('X-man')
c=C()
c.x()
print(c)

class BB:
    def printBB(self):
        print('no zuo no die')
b=BB()
b.printBB()
print(b)

class CC:
    def setxy(self,x,y):
        self.x=x
        self.y=y
    def printXY(self):
        print(self.x,self.y)

d=CC()
d.setxy(4,5)
d.printXY()
#print(d)
