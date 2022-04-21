#函數，帶參數
import random


def generate_random(number):
    for i in range(number):
        ran=random.randint(1,20)
        print(ran)


print(generate_random)


generate_random(5)
