import matplotlib.pyplot as plt

font = {'family': 'DFKai-SB',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # pass in the font dict as kwargs
plt.rc('axes', unicode_minus=False)

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.title("数与平方")
plt.xlabel("数值")
plt.ylabel("平方值")
plt.scatter(x_values, y_values, s=100, c='red')

# 设置每个坐标轴的取值范围（x轴取值，y轴取值）
plt.axis([0, 20, 0, 500])
plt.show()

# 参数1指定要以什么样的文件名保存图表，保存和代码的同目录下，第二个参数表示要将多余的空白区域剪掉，要保留空白区域，可省略第二个参数
# plt.savefig('squares_plot.png', bbox_inches='tight')
