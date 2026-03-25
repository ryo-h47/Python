import os
import shutil
import datetime

print(os.getcwd())

os.chdir('./Python_sample')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('./Python_sample')
os.chdir('./練習用ファイル')
os.chdir('./chapter3')

now=datetime.datetime.now()
shutil.move('move.csv','./'+now.strftime('%Y%m%d'))