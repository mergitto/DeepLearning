#多次元配列の計算をPythonで実装する
#A=一次元配列
#B=多次元配列


import numpy as np
A = np.array([1,2,3,4])
np.ndim(A) #次元数の取得
A.shape #配列の形状を取得

B = np.array([[1,2],[3,4],[5,6]])
np.ndim(B)
B.shape

#行列の内積
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("naiseki A * B")
print("A")
print(A)
print("B")
print(B)
print("A * B")
print(np.dot(A,B))

