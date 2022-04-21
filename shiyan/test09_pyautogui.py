import pyautogui
import pyperclip
import time

time.sleep(10)
while True:
    pyperclip.copy('我只是在用python做测试啦！！！')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.mouseUp()
    pyautogui.moveTo(1234, 1205)
    pyautogui.mouseDown()
    pyautogui.mouseUp
    time.sleep(3600)
