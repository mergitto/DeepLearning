# 数値微分の例
# coding: utf-8

import numpy as np
import matplotlib.pylab as plt

# 数値微分
def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h) #xを中心として、前後の差分を計算「中心差分」という

# (x + h) - x は「前方差分」と呼ばれる

def function_1(x):
    return 0.01*x**2 + 0.1*x


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

x = np.arange(0.0, 20.0, 0.1) # 0~20まで0.1刻みのx配列
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
