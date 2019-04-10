import re

import requests


def get_pic_url(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    html = res.text
    pic_url = re.findall(r'https*://[^\s]*?\.jpg', html, re.S)
    print(pic_url)
    # for key in pic_url:
    #     print(key + "\r\n")


for i in range(4860):
    print("开始爬", i, "页")
    url = "https://www.dbmeinv.com/?pager_offset=" + str(i)
    get_pic_url(url)
