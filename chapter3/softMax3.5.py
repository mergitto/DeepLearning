#出力層の設計（ソフトマックス関数：分類問題の活性化関数）

import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #オーバーフロー対策、簡単に値が大きくなるため入力の最大値を引く
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
print("Output softmax function")
print(softmax(a))

#ソフトマックス関数の性質の一つで総和が1.0になる
#この性質を利用してソフトマックス関数の出力から「確率」を求めることができる
print("Summary softmax function output")
print(np.sum(softmax(a)))
