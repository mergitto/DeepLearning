# coding: utf-8
# cf.http://d.hatena.ne.jp/white_wheels/20100327/p3
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        x[idx] = tmp_val - h
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 値を元に戻す
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        return grad


def function_2(x):
    if x.ndim == 1:
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1)


def tangent_line(f, x):
    d = numerical_gradient(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

if __name__ == '__main__':
    x0 = np.arange(-5, 5.0, 0.25)
    x1 = np.arange(-5, 5.0, 1.0)
    X, Y = np.meshgrid(x0, x1)
    X = X.flatten()
    Y = Y.flatten()
    grad = numerical_gradient(function_2, np.array([X, Y]) )

    print(X)
    print(Y)
    print(grad[1])
    print(grad[1])
    plt.figure()
    # gradにマイナスをかけるのは損失関数の符号を反転させることで、
    # 最小値を探す勾配降下法と最大値を探す勾配上昇法を探す問題は同じことになるからである
    plt.quiver(X, Y, -grad[0], -grad[1],color="#666666")
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()
