import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')

output=open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//output2.txt','w',encoding='UTF-8')
                 
for page in file:
    text=page.get_text()
    output.write(text)

output.close()
file.close()