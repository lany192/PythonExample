#!/usr/bin/env python  
# -*- coding: UTF-8 -*-

""" 
@author: Lany 
@file: Sougou.py 
@time: 2017/9/25 0025 16:18 
"""
import requests
import urllib
from bs4 import BeautifulSoup

res = requests.get('http://image.baidu.com/')
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.select('img'))
