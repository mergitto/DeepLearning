# coding: utf-8
# 乗算レイヤー

class MulLayer:
    # 初期化
    def __init__(self):
        self.x = None
        self.y = None

    # 順伝搬
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    # 逆伝搬
    def backward(self, dout):
        dx = dout * self.y # xとyをひっくり返す
        dy = dout * self.x

        return dx, dy


class AddLayer:
    def __init__(self):
        pass # 加算ノードの場合は初期化の必要がなく受け取ったx,yをそのまま出力する

    def forward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy
