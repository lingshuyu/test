'''
print(type(len))
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
a=New_int(3)
b=New_int(5)
print(a+b)
print(a-b)

class int(int):
    def __add__(self, other):
        return int.__sub__(self,other)

a=int('5')
b=int('3')
print(a+b)
'''
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self,other)

a=Nint(5)
b=Nint(3)
print(a+b)
print(1+b)

