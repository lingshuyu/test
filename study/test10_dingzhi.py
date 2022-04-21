import time as t
'''
t1 = t.localtime()
print(t1)
class A():
    def __str__(self):
        return '小甲鱼是帅哥！'
a=A()
print(a)
class B():
    def __repr__(self):
        return '小甲鱼是帅哥！'
b=B()
print(b)
print(t1)

'''

class MyTimer():
    def __init__(self):
        self.unit =['年','月','日','时','分','秒']
        self.prompt='未计时开始'
        self.lasted=[]
        self.begin=0
        self.end=0


    def __str__(self):
        return self.prompt

    __repr__ = __str__
    #开始计时
    def start(self):
        self.begin=t.localtime()
        self.prompt='提示'
        print('计时开始')
    #停止计时
    def stop(self):
        if not self.begin:
            print('提示，先调用start')
        else:
            self.end=t.localtime()
            print('计时结束')
    #内部方法，计算运行时间
    def _calc(self):
        self.lasted=[]
        self.prompt='总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]+self.unit[index])

        print(self.prompt)
t2=MyTimer()
t2.start()
t2.stop()
print(t2)

