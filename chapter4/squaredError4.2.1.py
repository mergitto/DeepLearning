#2乗和誤差

import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

#「2」を正解とする
t = np.array([0,0,1,0,0,0,0,0,0,0]) #正解が一つのみ(one-hot表現)

#正解と同じ「2」の確率が最も高くなる場合
y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
print("正解と同じデータの確率が大きくなる場合の誤差")
print(mean_squared_error(y, t))

#正解と異なる「7」の確率が最も高くなる場合
y = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])
print("正解と異なるデータの確率が大きくなる場合の誤差")
print(mean_squared_error(y, t))


