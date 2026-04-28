import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')
page=file[1]

image=open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//image.png','rb')

position=fitz.Rect(500,20,600,70)
position2=fitz.Rect(490,5,590,50)

page.insert_image(position,stream=image.read())
page.add_stamp_annot(position2,stamp=0)

file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//image.pdf')
file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//stamped.pdf')

file.close()