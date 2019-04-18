import matplotlib.pyplot as plt
from pylab import mpl

# 设置字体，这样才能显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 绘制散点图(传如一对x和y坐标，在指定位置绘制一个点)
plt.scatter(2, 4)
# 设置输出样式
plt.scatter(3, 5, s=200)
plt.title("绘制一个点")
plt.show()
