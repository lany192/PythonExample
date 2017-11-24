# coding=utf-8
import requests
from bs4 import BeautifulSoup

res = requests.get('http://pic.yesky.com/c/6_60300.shtml')
soup = BeautifulSoup(res.text, 'html.parser')
images = soup.select('img')
for image in images:
    title = image.get('alt')
    url = image.get('src')
    print(title, url)
