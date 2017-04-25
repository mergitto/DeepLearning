#ステップ関数をグラフで描画
#描画される図からわかることは0を境にして出力が0から1に切り替わることである
#この形状から「階段関数」と呼ばれることもある
#sigmoid.pyを実行してみて描画されたグラフを比較するとよい

import numpy as np
import matplotlib.pylab as plt

x = np.array([-1.0, 1.0, 2.0])
y = x > 0
print(y)
y = y.astype(np.int)
print(y)

def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #y軸の範囲を指定
plt.show()

x = np.arange(-3.0, 3.0, 1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
