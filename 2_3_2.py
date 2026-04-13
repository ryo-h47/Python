import requests
import bs4

html=requests.get('https://crawler2.sbcr.jp/pc/')
soup=bs4.BeautifulSoup(html.text,'lxml')

print(soup.find('div').find('h1'))
print(soup.find('div',class_='article-box'))
print(soup.find('div',id='pjax-content'))
print(soup.find('img',attrs={'alt':'SB Creative'}))

for script in soup.find_all(class_='article-box'):
    print(script.find('h3'))

for script in soup.find_all(class_='article-box'):
    print(script.find('a').get('href'))

for script in soup.find_all(class_='article-box'):
    script2=script.find(class_='block-day clearfix')
    
    script2.span.extract()
    print(script2.text)