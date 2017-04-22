#ReLU関数の実装

import numpy as np

def relu(x):
    return np.maximum(0, x)

print(relu(1.6))
print(relu(-1.6))
