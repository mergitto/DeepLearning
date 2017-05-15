# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # ガウス分布で初期化

    # 予測する
    def predict(self, x):
        return np.dot(x, self.W)

    # 損失関数の値を求める
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

x = np.array([0.6, 0.9]) # 入力データ
t = np.array([0, 0, 1]) # 正解ラベル

net = simpleNet()
print('重みパラメータ')
print(net.W)

f = lambda w: net.loss(x, t)
print(f(x))
dW = numerical_gradient(f, net.W)

print(dW)
