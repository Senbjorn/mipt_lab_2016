import matplotlib.pyplot as plt
import numpy as np

b = 0.5
a = 3
x = np.arange(0, 12, 0.001)
y = sum([b ** i * np.cos(a ** i * np.pi * x) for i in range(100)])
plt.plot(x, y)
plt.show()