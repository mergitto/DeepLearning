#シグモイド関数の実装
#step.pyと異なりsigmoid.pyを実行した時に描画されるグラフは曲線であることがわかる
#これがニューラルネットワークにおいて重要となる

import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
