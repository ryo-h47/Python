import pandas as pd

data=pd.read_excel('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//sales2020.xlsx')
data3=pd.pivot_table(data,index=['年度','四半期'],columns='事業',values='売上高',aggfunc='sum')

data3.to_csv('output.csv',index=True)