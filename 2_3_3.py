import bs4
import requests

html=requests.get('https://crawler2.sbcr.jp/pc/')
soup=bs4.BeautifulSoup(html.text,'lxml')

for script in soup.find_all(class_='article-box'):
    url=script.find('a').get('href')

    html2=requests.get(url)
    soup2=bs4.BeautifulSoup(html2.text,'lxml')

    title=soup2.find('h2').text

    soup3=soup2.find(class_='block-day clearfix')
    soup3.span.extract()
    rdate=soup3.text.strip()

    price=soup2.find(class_='block-price gf-rubik').text

    print(title)
    print(rdate)
    print(price)
    print('-----')