import numpy as np

class Affine:
    def __init__(self, W, b):
        self.W =W
        self.b = b
        self.x = None
        self.original_x_shape = None
        # 重み・バイアスパラメータの微分
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)


        return dx

X = np.random.rand(2)
W = np.random.rand(2,3)
B = np.random.rand(3)

print(X.shape)
print("X:",X)
print(W.shape)
print("W:",W)
print(B.shape)
print("B:",B)

print("X * W", np.dot(X, W))
Y = np.dot(X, W) + B
print("Y",Y)

af = Affine(W,B)
afY = af.forward(X)
print("forward",afY)
print(af.forward(X).shape)
print("dy * Wt")
print(np.dot(afY, W.T))
print(np.dot(afY, W.T).shape)
