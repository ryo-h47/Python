import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')

file.move_page(1,to=0)

file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//moved.pdf')

file.close()