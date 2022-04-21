'''

a=list()
b='i love you'
b=list(b)
print(b)
number=[1,2,4,45,67,87,32,3,6]
print(list(reversed(number)))
print(list(sorted(number)))



def MyFirstFunction():
    print('这是我创建的第一个函数')
    print('我表示很激动')
def MySecondFunction(name):
    print(name+'这是我创建的第一个函数')
print(MyFirstFunction())
def add(num1,num2):
    result=num1+num2
    print(result)

print(add(4,5))

def MyFirstFunction(name):
    print('这是我创建的第一个函数'+name+'111')
print(MyFirstFunction('唐成亮'))

def saysome(name,words):
    print(name+'__'+words)
saysome('唐成亮','林小翠')

def test(*params,exp):
    print('参数长度',len(params),exp)
    print('第二个参数',params[1])
test(3,9,5,'tcl',exp=3)

def hello():
    print('hello world!')
print(hello())

def discounts(price,rate):
    final_price=price * rate
   # print('试图打印原来的价格',old_price)
    old_price=50
    print('修改后的old_price的值：',old_price)
    return final_price
old_price=float(input('请输入原价：'))
rate=float(input('请输入折扣率：'))
new_price=discounts(old_price,rate)
print('打折后的价格：',new_price)
'''
count=5
def MyFun():
    global count
    count = 10
    print(10)

print(MyFun())


def fun1():
    print('fun1正在被调用。。。。')
    def fun2():
        print('fun2正在被调用。。。。')

print(fun1())

def FunX(x):
    def FunY(y):
        return x*y
    return FunY
i= FunX(8)
print(i(5))