import matplotlib.pyplot as plt
import math
import numpy as np


y1 = np.array([0] * 11, float)
y2 = np.array([0] * 101, float)
x = 0

def f(y, x):
    dy = 1 - math.sin(1.25 * x + y) + 0.5 * y / (x + 2)
    return dy

def rk4(y, h, leng):
    global x
    for i in range(leng - 1):
        k1 = f(y[i], x + i * h)
        k2 = f(y[i], x + i * h) + h / 2 * k1
        k3 = f(y[i], x + i * h) + h / 2 * k2
        k4 = f(y[i], x + i * h) + h * k3
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


x1 = np.linspace(0, 1, 11)
x2 = np.linspace(0, 1, 101)
rk4(y1, 0.1, 11)
rk4(y2, 0.01, 101)
plt.plot(x1, y1, x2, y2)
plt.grid()
plt.show()