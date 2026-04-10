import pyautogui
import datetime
import shutil

print(pyautogui.size())
print(pyautogui.position())
pyautogui.moveTo(400,500)
pyautogui.click(400,500)
pyautogui.press('enter',presses=3)
pyautogui.typewrite('password')
pyautogui.alert('Hi! How are you doing?')

result=pyautogui.confilm('CSVファイルを移動します。よろしいですか?')

now=datetime.datetime.now()
if result=='OK':
    shutil.move('finance.csv','./'+now.strftime('%Y%m%d'))

result=pyautogui.prompt('日付を入力してください(YYYYMMDD形式)')

if len(result)==6:
    print(result)
else:
    pyautogui.alert('日付が入力されていません')

pyautogui.screenshot('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter3//screenshot.png',
                     region=(0,270,1100,90))

position=pyautogui.locateOnScreen('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter3//save.png')
print(position)