import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')

print(file.page_count)
print(file.get_toc())

file.save('saved.pdf')

file.close()

print(file.is_closed)

if file.close()==False:
    file.close()

