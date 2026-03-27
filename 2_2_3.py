import zipfile
import os

os.getcwd()
os.chdir('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter3')

zf=zipfile.ZipFile('compress.zip','w',compression=zipfile.ZIP_DEFLATED)
zf.write('compress.csv')
zf.close()

zf=zipfile.ZipFile('unzip.zip','r')
zf.extractall()
zf.close()