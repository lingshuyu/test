class C:
    def __init__(self):
        self.x='X-man'
c=C()
print(c.x)

class B:
    def __getattribute__(self, name):
        print('getattribute')
        return super().__getattribute__(name)
    def __getattr__(self, name):
        print('getattr')
    def __setattr__(self, name, value):
        print('setattr')
        super().__setattr__(name,value)
    def __delattr__(self, name):
        print('delattr')
        super().__delattr__(name)
b=B()
b.x
print(b)

class Rectangle():
    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height

    def __setattr__(self, name, value):
        if name =='square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(name,value)

    def getArea(self):
        return self.width * self.height

r=Rectangle(4,5)
r.getArea()
print(r.getArea())
print(r.height)
print(r.width)