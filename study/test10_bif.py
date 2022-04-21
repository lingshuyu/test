'''
class A:
    pass
class B(A):
    pass
i=issubclass(B,A)
print(i)
'''


class C:
    def __init__(self, size=10):
        self.size = size

    def get_size(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(get_size, setSize, delSize)


c = C()
c.x = 1
print(c.size)
