import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')
page=file[1]

text=page.get_text()

print(text)

file.close()