import requests

html=requests.get('https://crawler2.sbcr.jp/pc/',params={'s':'業務改善','sort':'new'})
print(html.ok)
print(html.text)

