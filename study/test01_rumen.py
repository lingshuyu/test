

import random

#定義函數
def generate_random():
    for i in range(10):
        ran=random.randint(1,20)
        print(ran)


print(generate_random) #打印函數名


generate_random() #調用函數名，找到函數併執行函數

