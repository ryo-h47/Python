import pandas as pd

project=pd.read_excel('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//project.xlsx')
staff=pd.read_excel('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//staff.xlsx')
order=pd.read_excel('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//order.xlsx')
item=pd.read_excel('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//item.xlsx')

data=project.merge(staff,on='社員番号')
print(data)

data2=order.merge(item,on='商品ID')
print(data2)

data3=order.merge(item,how='left',on='商品ID')
print(data3)

data4=order.merge(item,how='right',on='商品ID')
print(data4)