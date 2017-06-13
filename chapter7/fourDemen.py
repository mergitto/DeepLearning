import sys, os
sys.path.append(os.pardir)
from common.util import im2col
import numpy as np

# im2colを理解する
print("==================im2col=======================")
print('入力サイズ（3､3）ストライド1、フィルター（2､2）パディング０')
x1 = np.random.rand(1, 1, 4, 4)
col1 = im2col(x1, 3, 3, stride=1, pad=0)


#print('入力サイズ（7､7）ストライド2、フィルター（3､3）パディング０')
#x1 = np.random.rand(1, 1, 7, 7)
#col1 = im2col(x1, 3, 3, stride=2, pad=0)

#print('入力サイズ（7､7）ストライド1、フィルター（3､3）パディング０')
#x1 = np.random.rand(1, 1, 7, 7)
#col1 = im2col(x1, 3, 3, stride=1, pad=0)

#print("==================paddingについて===================")
#pad = 2
#print("x1")
#print(x1)
#x1Pad = np.pad(x1, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
#print("x1Pad")
#print(x1Pad)

print("==================Pooling=======================")
# Poolingについて理解する
class Pooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)

        # 展開(1)
        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h*self.pool_w)

        # 最大値(2)
        out = np.max(col, axis=1)
        # 整形(3)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        return out

# 1.入力データを展開する
# 2.行ごとに最大値を求める
# 3.適切な出力サイズに整形する
#layer = Pooling(pool_h=2, pool_w=2, stride=2)
#x = np.random.rand(1,2,4,4)
#print(layer.forward(x))
