'''
def recursion():
    return recursion()
print(recursion())

#分递归形式
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
number = int(input('请输入一个正整数：'))
result = factorial(number)
print('%d的阶乘是：%d' %(number,result))

#递归
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input('请输入一个正整数：'))
result = factorial(number)
print('%d的阶乘是：%d' %(number,result))
#迭代
def fab(n):
    n1=1
    n2=1
    n3=1

    if n<1:
        print('输入错误')
        return -1
    while (n-2)>0:
        n3=n2+n1
        n1=n2
        n2=n3
        n -= 1

    return n3

result = fab(20)
if result != -1:
    print('总共有%d对兔子诞生！' % result)
'''
def fab(n):
    if n<1:
        print('输入错误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

result = fab(20)
if result != -1:
    print('总共有%d对兔子诞生！' % result)

    def hanoi(n,x,y,z):
        if n==1:
            print(x,'--->',z)
        else:
            hanoi(n-1,x,z,y)
            print(x, '--->', z)
            hanoi(n - 1, y, x, z)

    n=int(input('输入层数：'))
    print(hanoi(n,'X','Y','Z'))