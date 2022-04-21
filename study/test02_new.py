'''print("i love you tcl")
print('520'+'1314')
print('520'+'1314\n'*4)
str = r'C:\now'

print(str)
teacher = 'tcl'
print(teacher)
frist = 3
second = 5
thrid =frist+second
print(thrid)

import random
secret = random.randint(1,20)
print('--------')

temp = input('猜数字：')
guess = int(temp)
while guess != secret:
    if guess<secret:
        print('猜小了')
    else:
        print('猜大了')
    temp = input('猜错了，重新来一次吧。')
    guess = int(temp)


if guess == secret:
    print('猜中啦')
print('游戏结束,恭喜你')
'''
a=3**2
print(a)





