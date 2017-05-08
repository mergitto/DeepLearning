# 学習に関するテクニック
本章ではニューラルネットワークの学習においてキーとなるものを説明します 
取り上げるテーマは
- 最適な重みパラメータを探索する最適化手法
- 重みパラメータの初期値
- ハイパーパラメータの設定方法
どれもニューラルネットワークの学習において重要なテーマである 

また過学習の対応策として
- Weight decay
- Dropout
などの正則化手法の概要説明と実装を行う

最後に
- Batch Normalization
という手法の説明をおこなう

### パラメータの更新
損失関数の値をできるだけ小さくするパラメータを見つけることを**最適化**という 
これまで勾配を使って徐々に最適なパラメータへと近づけて行ったが、それのことを**確率的勾配降下法**と呼び、**SGD**とよぶ 

### SGDの弱点
SGDは単純で実装も簡単だが、問題によっては勾配が本来の最小値ではない方向をさして非効率な場合があるのでそれに代わる手法として以下の3つの手法を説明する
- Momentum
実装したものはcommon/optimizer.pyにある 
物理でいう速度にあたる変数が登場し、何も力を受けない時には徐々に減速するような役割を担う 

- AdaGrad
ニューラルネットワークの学習では学習係数が小さすぎると時間がかかり、大きすぎると発散してしまい正しい学習を行うことができない 
この学習係数に関する有効なテクニックとして、学習係数を学習が進むにつれて小さくしていくという方法がある 
パラメータの要素ごとに適応的に更新ステップを調整するのである 

- Adam
MomentumとAdaGradを融合したような手法 
ハイパーパラメータの「バイアス補正」が行われるのも特徴 

同じディレクトリにある
- optimizer_conpare_naive.py
- optimizer_conpare_mnist.py
~naive.pyは
```
f(x,y) = 1 / 20 x^2 + y^2
```
の数式を各手法によるパラメータ更新を計算している 

~mnist.pyはMNISTデータセット(手書き数字)を対象にパラメータの更新を行なっている 


とはいえ、多くの研究ではSGDを含めそれぞれに特徴と得意・不得意があるため実験によって変更するのが良さそう！ 
一般的にはSGDよりも他の3つの手法の方が早く学習でき、認識性能も高くなることが多い 

### Batch Normalization
Batch Normalizationには次の３つの利点がある
- 学習を早く進行させる(学習係数を大きくすることができる)
- 初期値に依存しない
- 過学習を抑制する
batch_norm_test.pyを実行すると学習の様子が表示される。点線がBatch Normを使用しなかった場合、実線が使用した場合である 

**過学習**
過学習が起きる原因として主に次の２つの理由が考えられる
- パラメータを大量にもち、表現力の高いモデルである
- 訓練データが少ない

**Weight decay**
過学習を抑制する手法にWeight decay(荷重減衰)という手法がある。学習の過程で大きな重みを持つことに対してペナルティを課すことで過学習を抑制しようというもの 
簡単に実装できて、ある程度過学習を抑制できるのでお手軽である。 
上の2つの要件をわざと外して過学習を発生させたものをoverfit_weight_decay.pyにて実行することができる 
MNISTデータを300個だけに限定し、複雑性を高めるために７層のネットワーク、各層のニューロンを100個、活性化関数をReLUを用いている 
weight_decay_lambdaのコメントアウトを変更するとで過学習抑制のために用いられているWeight decayを用いるかどうかを変更することができる

**Dropout**
過学習を抑制する手法としてWeight decayを紹介したが、ニューラルネットワークのモデルが複雑になってくるとそれだけでは対応が困難になってしまう
Dropoutは訓練時に隠れ層のニューロンをランダムに選び出し消去する。訓練時にはデータが流れるたびにニューロンをランダムで消去するが、各ニューロンの出力に対して訓練時に消去した割合を乗算して出力する
訓練を実装したものをoverfit_dropout.pyに実装している 
Dropoutの有無はoverfit_dropout.pyにて変更可能 

### ハイパーパラメータの検証
ニューラルネットワークには重みやバイアスといったパラメータとは別にハイパーパラメータと呼ばれる、各層のニューロン数やバッチサイズ、パラメータ更新の際の学習係数、Weight decay等である 
ハイパーパラメータの決定には試行錯誤が伴うが、できるだけ効率的にハイパーパラメータの値を探索する方法について説明する 
※ハイパーパラメータはテストデータを使って評価してはいけない。テストデータに対して過学習を起こしテストデータのためだけのハイパーパラメータになる可能性があるからである 

### ハイパーパラメータの最適化
ハイパーパラメータ最適化の重要なポイントは規則的な探索よりも、ランダムにサンプリングして探索する方が良い結果が出ることである 
ディープラーニングの学習には多くの時間が必要になるため、ハイパーパラメータの最適化には一回の評価に要する時間を短縮することが有効である 
これらをまとめると次のステップを繰り返すことになります
1. ハイパーパラメータの範囲を設定する
1. 設定されたハイパーパラメータの範囲からランダムにサンプリングする
1. ステップ1でサンプリングされたハイパーパラメータの値を使用して学習を行い、検証データで認識精度を評価する（この時エポックは小さく設定）
1. ステップ1とステップ2をある回数繰り返し、それらの認識精度の結果から、ハイパーパラメータの範囲を狭める
これらのステップを繰り返し、ハイパーパラメータの値を絞っていき、ある程度絞り込んだ段階で、その範囲の中からハイパーパラメータの値を一つ取り出す。これがハイパーパラメータ最適化の1つの手法です。

### ハイパーパラメータ最適化の実装
MNISTデータセットを使用してハイパーパラメータ最適化を実装したものをhyperparameter_optimization.pyにて実装している 
ここでは学習係数とWeight decayの強さをコントロールする係数の2つを探索している

### まとめ
本章では、ニューラルネットワークの学習を行う上で重要なテクニックをいくつか紹介しました。 
Batch Normalization,Dropoutなど、どれも欠かせない技術である
- パラメータ更新にはSGD(確率的勾配降下法)、Momentum,AdaGrad,Adamなどがある
- 重みの初期値の与え方は正しい学習を行う上で重要である
- 重みの初期値として、「Xavierの初期値」「Heの初期値」が有効である
- Batch Normalizationを用いることで学習を早く進めることができる
- 過学習を抑制するための正則化の技術としてWeight decayやDropoutがある
- ハイパーパラメータの探索は良い値が存在する範囲を狭めながら進めるのが効率の良い方法である