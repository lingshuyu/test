from __future__ import unicode_literals
import wxpy
import requests
from threading import Timer

bot = None


def get_news():
    url = 'http://open.iciba.com/dsapi/'
    r = requests.get(url)
    print(r.json())
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation


def login_wechat():
    global bot


#    bot=Bot()
def send_news():
    if bot == None:
        login_wechat()
    try:
        my_friend = bot.friends().search(u'Tcl阿亮')[0]
        my_friend.send(get_news()[0])
        my_friend.send(get_news()[1][5:])
        my_friend.send(u'我是自动人')
        t = Timer(360, send_news())
        t.start()
    except:
        print(u'失败')


if __name__ == '__main__':
    send_news()
