import fitz
import datetime

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')
page=file[1]

position=fitz.Rect(420,10,570,70)
position2=fitz.Rect(200,300,500,600)

now=datetime.datetime.now()
text=now.strftime('%Y年%m月%d日')+' 編集部'
text2='社外秘'

page.insert_textbox(position,text,fontsize=10,fontname='japan')

for page in file:
    page.insert_textbox(position2,text2,fontsize=60,fontname='japan',color=(92/255,192/255,92/255),fill_opacity=0.5)

file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//watermark.pdf')
file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//watermark2.pdf')

file.close()