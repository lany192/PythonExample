import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, s=100)

# 设置每个坐标轴的取值范围（x轴取值，y轴取值）
plt.axis([0, 1100, 0, 1100000])
plt.show()
