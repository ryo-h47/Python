import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Meiryo'

data=pd.read_excel('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//sales2020.xlsx')

data2=data.query('事業=="ゲーム"')

data2.plot(kind='bar',x='四半期',y='売上高')
plt.show()

data3=pd.pivot_table(data,index=['年度','四半期'],columns='事業',values='売上高',aggfunc='sum')

data3.plot(kind='bar',stacked=True)
plt.show()
