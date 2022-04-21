def login(username, password):
    uname = 'admin123'
    pwd = '112233'

    for i in range(3):
        if username == uname and password == pwd:
            print('登錄成功')
            break
        else:
            print('登錄失敗')
            username = input('請輸入用戶名：')
            password = input('請輸入密碼：')

    else:
        print('賬戶鎖定')


username = input('請輸入用戶名：')
password = input('請輸入密碼：')

login(username, password)
