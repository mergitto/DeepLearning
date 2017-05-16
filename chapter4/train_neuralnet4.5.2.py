# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet # 同じディレクトリのtwo_layer_net.pyからインポートしている

# データの読み込み
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# 勾配法による更新の回数-繰り返し(iterate)の回数を今回は10000回としている
iters_num = 10000  # 繰り返しの回数を適宜設定する
train_size = x_train.shape[0] # 訓練データ数
batch_size = 100 # バッチ数、訓練データからランダムにバッチ数分取り出す
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

# epoch:エポック、学習において訓練データを全て使い切った時の回数に対応する
# 例;10000個の訓練データに対して100個のミニバッチで学習する場合、確率的勾配降下法を100回繰り返したら、
# １エポック = 100回　となる

# 1エポックあたりの繰り返し数
iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    # ミニバッチの取得
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 勾配の計算
    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)

    # パラメータの更新
    # p107
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
        #print(grad[key])

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    # 1エポック毎に認識精度を計算
    if i % iter_per_epoch == 0:
        print(i)
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

# グラフの描画
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()
