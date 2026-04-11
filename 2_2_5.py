import webbrowser
import time
import pyautogui
import os
import datetime
import shutil

webbrowser.open('nihonzuno.co.jp/sample.html')
time.sleep(3)

os.chdir('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter3')
position=pyautogui.locateOnScreen('text.png')
if position!=None:
    pyautogui.click(position)
    pyautogui.typewrite('password')

position=pyautogui.locateOnScreen('button.png')
if position!=None:
    pyautogui.click(position)
    time.sleep(3)

os.chdir('C://Users//Owner//ダウンロード//')

now=datetime.datetime.now()
folder=now.strftime('%Y%m%d')

if os.path.exists(folder)==False:
    os.mkdir(folder)

file='finance.csv'
shutil.move(file,folder)