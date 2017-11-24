#!/usr/bin/env python  
# -*- coding: UTF-8 -*-

""" 
@author: Lany 
@file: readfile.py 
@time: 2017/10/13 0013 8:52 
"""
import pymysql

file = open("www.txt")
userIndex = 0
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='admin',
                     db='www_db',
                     charset='utf8'
                     )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

while 1:
    line = file.readline()
    if not line:
        break
    pass
    userIndex = userIndex + 1
    print(u'记录：', userIndex, line)
    items = line.split("----")
    print(u'邮箱:', items[0])
    print(u'密码1:', items[1])
    print(u'姓名:', items[2])
    print(u'身份证:', items[3])
    print(u'密码2:', items[4])
    print(u'手机:', items[5])

    sql=cmd = u"INSERT INTO user_tb (user_name , id_card , email, phone, pwd , pwd2) VALUES ('{}', '{}', '{}', '{}','{}', '{}')".format(items[2],items[3], items[0], items[5], items[1], items[4])

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        print('数据插入成功')
    except Exception as e:
        # 发生错误时回滚
        print(u'出错=============:', userIndex, e)
        db.rollback()
cursor.close()
db.close()
print("操作结束")
