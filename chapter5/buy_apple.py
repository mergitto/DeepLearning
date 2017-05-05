# coding: utf-8
# 第5章図5-16の順伝搬と逆伝搬の計算を行う
from layer_naive import * # 同じディレクトリの関数を呼び出している


apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward シンプルな計算を行う
# りんご値段と個数を計算してからそこに税をたす
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

# backward 各変数の微分の値を求める 計算は逆になる
# まず税の微分を求めてからりんごの値段と個数の微分を計算する
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print("price:", int(price))
print("dApple:", dapple)
print("dApple_num:", int(dapple_num))
print("dTax:", dtax)
