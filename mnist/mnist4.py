import tensorflow as tf  # 深度学习库，Tensor 就是多维数组

import matplotlib.pyplot as plt
print('当前tensortflow版本:{0}'.format(tf.__version__))
print('当前keras版本:{0}'.format(tf.keras.__version__))
mnist = tf.keras.datasets.mnist  # mnist 是 28x28 的手写数字图片和对应标签的数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 分割数据集

x_train = tf.keras.utils.normalize(x_train, axis=1)  # 把数据值缩放到 0 到 1
x_test = tf.keras.utils.normalize(x_test, axis=1)

# for index in range(10):
#     plt.figure()
#     plt.imshow(x_train[index])
#     plt.colorbar()
#     plt.grid(False)
#     plt.xlabel("Classification label: {}".format(y_train[index]))
#     plt.show()


model = tf.keras.models.Sequential()  # 基础的前馈神经网络模型
# model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))  # 把图片展平，这里指定了input_shape 参数，否则模型无法通过 model.save() 保存
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # 简单的全连接图层,，128 个单元，激活函数为 relu
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # 输出层 ，10 个单元， 使用 Softmax 获得概率分布

model.compile(optimizer='adam',  # 默认的较好的优化器
              loss='sparse_categorical_crossentropy',  # 评估“错误”的损失函数，模型应该尽量降低损失
              metrics=['accuracy'])  # 评价指标

model.fit(x_train, y_train, epochs=3)  # 训练模型

val_loss, val_acc = model.evaluate(x_test, y_test)  # 评估模型对样本数据的输出结果
print('模型的损失值:', val_loss)
print('模型的准确度:', val_acc)
# 保存模型
# OUT_MODEL_DIR = 'model'
# model.save(OUT_MODEL_DIR + '/mnist4.h5')

# Save tf.keras model in HDF5 format.
keras_file = "model/mnist4_model.h5"
tf.keras.models.save_model(model, keras_file)

# Convert to TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_keras_model_file(keras_file)
tflite_model = converter.convert()
open("model/mnist4_model.tflite", "wb").write(tflite_model)
