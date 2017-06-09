import sys, os
sys.path.append(os.pardir)
from common.util import im2col
import numpy as np

print('入力サイズ（3､3）ストライド1、フィルター（2､2）パディング０')
x1 = np.random.rand(1, 1, 3, 3)
col1 = im2col(x1, 2, 2, stride=1, pad=0)


print('入力サイズ（7､7）ストライド2、フィルター（3､3）パディング０')
x1 = np.random.rand(1, 1, 7, 7)
col1 = im2col(x1, 3, 3, stride=2, pad=0)

print('入力サイズ（7､7）ストライド1、フィルター（3､3）パディング０')
x1 = np.random.rand(1, 1, 7, 7)
col1 = im2col(x1, 3, 3, stride=1, pad=0)
