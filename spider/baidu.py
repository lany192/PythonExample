#!/usr/bin/env python  
# -*- coding: UTF-8 -*-

""" 
@author: Lany 
@file: baidu.py 
@time: 2017/9/25 0025 17:33 
"""
#coding=utf-8
import urllib.request
import re

def getHtml(url):

    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    #print(html)
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" width'
    #re.compile(reg)把正则表达式转换成re的正则对象
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print(imglist)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % imgurl[-20:-4])
        x+=1


html = getHtml("https://tieba.baidu.com/p/4658587322")

print(getImg(html))