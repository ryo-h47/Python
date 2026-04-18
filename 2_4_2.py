import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')
file2=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample2.pdf')

file.insert_pdf(file2,start_at=1)

file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//merged.pdf')

file.close()
file2.close()