import fitz

file=fitz.open('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//sample.pdf')

for page in file:
    positions=page.search_for('アプリ')
    page.add_highlight_annot(positions)

file.save('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter5//highlighted2.pdf') 

file.close()