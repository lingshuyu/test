

class Parent:
    def hello(self):
        print('正在调用父类的方法')
class Child(Parent):
    pass
p = Parent
p.hello(0)
print(p)
c=Child
c.hello(0)
print(c)

import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print('我的位置是：',self.x,self.y)

class GoldFish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有吃的')
            self.hungry = False
        else:
            print('太棒了，吃不下了')


f=Fish()
f.move()
print(f)
g=GoldFish()
g.move()
print(g)

s=shark()
s.move()
print(s)

class Base1:
    def foo1(self):
        print('foo1,Base1')
class Bas2:
    def foo2(self):
        print('foo2,Base2')

class C(Base1,Bas2):
    pass
c=C()
c.foo1()
print(c)