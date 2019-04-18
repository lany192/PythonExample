import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'DFKai-SB',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # pass in the font dict as kwargs
plt.rc('axes', unicode_minus=False)

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x ** 2)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.title("标题")
plt.ylim(-1.2, 1.2)
plt.legend()
plt.show()
