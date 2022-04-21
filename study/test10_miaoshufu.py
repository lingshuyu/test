class MyDecriptor:
    def __get__(self, instance, owner):
        print('getting',self,instance,owner)
    def __set__(self, instance, value):
        print('setting',self,instance,value)

    def __delete__(self, instance):
        print('delete',self,instance)

class Test:
    x=MyDecriptor()

test=Test()
print(test.x)

class Celsius:
    def __init__(self,value =26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value)-32)/1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

temp = Temperature()
print(temp.cel)
temp.cel = 30
print(temp.fah)

class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

c1=CountList(1,3,5,7,9)
c2=CountList(2,4,6,8,10)
c=c1[1]
print(c)
b=c1.count
print(b)