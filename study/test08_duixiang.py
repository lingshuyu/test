class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    def climb(self):
        print('我正在很努力的向前爬')
    def run(self):
        print('我正在飞快的向前爬')
    def bite(self):
        print('咬死你咬死你')
    def eat(self):
        print('有的吃，真满足')
    def sleep(self):
        print('困了，睡了，晚安zzzzzz')


tt=Turtle()
print(tt.climb())

