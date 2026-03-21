import pandas as pd

data1='C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//Meguro.xlsx'
data2='C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//Mejiro.xlsx'

data1_2=pd.read_excel(data1)
data2_2=pd.read_excel(data2)

data=pd.concat([data1_2,data2_2])

print(data)

data.to_excel('customer.xlsx',sheet_name='list',index=False)