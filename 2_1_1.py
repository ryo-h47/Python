import pandas as pd

path='C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//data.xlsx'

data=pd.read_excel(path)

print(data.head(3))
print(data.tail(3))
print(data.info())
print(data.describe(include='all'))
print(len(data))
print(len(data.columns))
print(data.loc[1,'案件名'])
print(data.iloc[1,1])

print(data.sort_values(by='納品期限'))
print(data.sort_values(by='納品期限',ascending=False))
print(data.sort_values(by=['納品期限','金額']))
print(data.sort_values(by=['納品期限','金額'],ascending=[True,False]))

print(data.query('金額<60000'))
print(data.query('30000<=金額<60000'))
print(data.query('種別=="スポット"'))
print(data.query('金額<60000 & 種別=="スポット"'))

print(data.groupby('種別').sum(numeric_only=True))
print(data.groupby('種別').mean(numeric_only=True))
print(data.groupby('種別').max(numeric_only=True))
print(data.groupby('種別').min(numeric_only=True))

print(pd.pivot_table(data,index='責任者',columns='種別',values='金額',aggfunc='sum'))


print(pd.pivot_table(
    data,
    index=[data['受注日'].dt.year,data['受注日'].dt.month],
    columns='種別',
    values='金額',
    aggfunc='sum'))