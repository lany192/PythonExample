import re
import time
from urllib.error import ContentTooShortError
from urllib.request import urlretrieve

import requests


# 下载保存图片
def auto_down_pic(url, filename):
    try:
        urlretrieve(url, filename)
    except ContentTooShortError:
        print("Network conditions is not good.Reloading.")
        auto_down_pic(url, filename)


# 查找照片并下载
def get_pic_url(url):
    html = requests.get(url).text
    pic_list = re.findall(r'https*://[^\s]*?\.jpg', html, re.S)
    for key in pic_list:
        print(key + "\r\n")
        # 保存图片,注意images要提前创建
        pic_dir = "./images/"
        pic_name = pic_dir + str(int(time.time())) + ".jpg"
        auto_down_pic(key, pic_name)


# 第一页开始
for i in range(4860):
    print("开始爬", i, "页")
    url = "https://www.dbmeinv.com/?pager_offset=" + str(i)
    get_pic_url(url)
    time.sleep(3)  # 休眠3秒
