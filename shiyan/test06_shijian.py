import datetime
import time
import requests

def love_date():
    First_day=datetime.datetime(2016,6,8)
    Today=datetime.datetime.now()
    The_love_day=Today-First_day
    return The_love_day.days
t=str(love_date())
print('今天是我们相恋的{t}天'.format(t=t))
'''
def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    print(r.json())
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents,translation
]
'''



