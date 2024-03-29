#!/usr/bin/env python  
# -*- coding: UTF-8 -*-

"""
样例来源http://blog.csdn.net/DilemmaVF/article/details/66476862
@author: Lany 
@file: Sample1.py 
@time: 2017/11/24 0024 17:12 
"""
# 导入依赖库
import numpy as np  # 这是Python的一种开源的数值计算扩展，非常强大
import tensorflow as tf  # 导入tensorflow

A = 0.1
B = 0.8

##构造数据##
x_data = np.random.rand(100).astype(np.float32)  # 随机生成100个类型为float32的值
y_data = x_data * A + B  # 定义方程式y=x_data*A+B
##-------##

##建立TensorFlow神经计算结构##
weight = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
y = weight * x_data + biases
##-------##


loss = tf.reduce_mean(tf.square(y - y_data))  # 判断与正确值的差距
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 根据差距进行反向传播修正参数
train = optimizer.minimize(loss)  # 建立训练器

init = tf.initialize_all_variables()  # 初始化TensorFlow训练结构
sess = tf.Session()  # 建立TensorFlow训练会话
sess.run(init)  # 将训练结构装载到会话中

for step in range(2000):  # 循环训练2000次
    sess.run(train)  # 使用训练器根据训练结构进行训练
    if step % 20 == 0:  # 每20次打印一次训练结果
        print(step, sess.run(weight), sess.run(biases))  # 训练次数，A值，B值
