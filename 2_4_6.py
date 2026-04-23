import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')

file.new_page(1)

file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//added.pdf')

file.close()