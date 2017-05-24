import numpy as np
import matplotlib.pyplot as plt
import datetime
from collections import Counter
import csv


f = open('./pyDays.csv', 'r')
dataReader = csv.reader(f)
days = np.array( [] )

for gyou,row in enumerate(dataReader):
    for index, data in enumerate(row):
        if(index == 0 and gyou != 0): # プロジェクト作成日の行でタイトル行じゃないとき
            day = datetime.datetime.strptime(data, '%m/%d/%y')
            if(day < datetime.datetime.strptime('2016-10-01', '%Y-%m-%d')): #2016-10-01までのデータを使用する
                days = np.append(days, datetime.datetime.strptime(data, '%m/%d/%y'))

# 配列の中身を計算する
words = np.array( [] )
counts = np.array( [] )
counter = Counter(days)
tuples = []
for word, cnt in counter.most_common():
    tuples = tuples + [(word, cnt)]
# タプルをソートする（日付で）
tuples = sorted(tuples)

# タプルからプロットするために配列変換
for i in tuples:
    for index, value in enumerate(i):
        print(index,":",value)
        if(index == 0):
            words = np.append(words, value)
        else:
            counts = np.append(counts, value)


datum = np.zeros((0,words.size))
datum = np.r_[datum, words.reshape(1, -1)]
datum = np.r_[datum, counts.reshape(1, -1)]

print(datum)
plt.plot(datum[0], datum[1])
plt.show()
