import bs4
import requests
import pandas as pd

html=requests.get('https://crawler2.sbcr.jp/pc/')
soup=bs4.BeautifulSoup(html.text,'lxml')

data=[]

for script in soup.find_all(class_='article-box'):
    url=script.find('a').get('href')

    htmi2=requests.get(url)
    soup2=bs4.BeautifulSoup(htmi2.text,'lxml')

    title=soup2.find('h2').text

    soup3=soup2.find(class_='block-day clearfix')
    soup3.span.extract()
    rdate=soup3.text.strip()

    price=soup2.find(class_='block-price gf-rubik').text

    data.append([title,rdate,price])

print(data)

df=pd.DataFrame(data,columns=['タイトル','発売日','価格'])
df.to_excel('C://Users//Owner//Documents//GitHub//Python//Python_sample//練習用ファイル//chapter2//books.xlsx',sheet_name='books',index=False)