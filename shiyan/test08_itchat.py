import itchat
import time

print('扫一下弹出来的二维码')
itchat.auto_login(hotReload=True)
boom_remark_name = input('输入轰炸的微信备注，按回车键继续')
message = input('输入轰炸的内容，回车键开始轰炸')
boom_obj = itchat.search_friends(remarkName=boom_remark_name)[0]['UserName']
while True:
    time.sleep(0.5)
    print('正在轰炸。。。。')
    itchat.send_msg(msg=message, toUserName=boom_obj)
