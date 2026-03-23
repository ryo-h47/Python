import os
import datetime

folder='C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter3//'
file1=folder+'download.csv'
file2=folder+'rename.csv'

os.rename(file1,file2)

now=datetime.datetime.now()

subfolder=folder+now.strftime('%Y%m%d')

if os.path.exists(subfolder)==False:
    os.mkdir(subfolder)