import random
import os
secret=random.randint(1,10)
print(secret)
print(os.getcwd())
print(os.listdir('D:\\'))

print(os.name)

print(os.path.splitext('D:\lin.txt'))
import time
s=time.gmtime(os.path.getatime('D:\lin.txt'))
t=time.localtime(os.path.getatime('D:\lin.txt'))
print(s)
print(t)
