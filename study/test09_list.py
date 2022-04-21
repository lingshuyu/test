

list1 = [2,5,4,7,1,3]
print(list1)
list1.sort()
print(list1)

class MyList(list):
    pass

list2= MyList()
list2.append(6)
list2.append(5)
list2.append(7)
print(list2)

class A:
    def fun(self):
        print('我是A')

class B:
    def fun(self):
        print('我是B')

a=A()
b=B()
print(a.fun())

class Ball:
    def setName(self,name):
        self.name=name
    def kick(self):
        print('我叫%s,该死的' %self.name)
a=Ball()
a.setName('A')
print(a.kick())

class ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print('我叫%s,该死的' %self.name)
b=ball('土豆')
print(b.kick())

class Person:
    name='小甲鱼'

p=Person
print(p.name)

class person:
    __name='小甲鱼'
    def getname(self):
        return self.__name

p=person
print(p.__person__name())
