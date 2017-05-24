import xlrd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import locale
from collections import Counter


# Excelファイル読み込み
book = xlrd.open_workbook("pythonTest2.xlsx")
book1 = xlrd.open_workbook("pyDays.xlsx")

sheet = book.sheet_by_index(0)
sheet1 = book1.sheet_by_index(0)

cellA1 = sheet.cell(0, 0)
cellA2 = sheet.cell(1, 0)
cellB1 = sheet.cell(0, 1)
cellB2 = sheet.cell(1, 1)

#print(cellA1.value)
#print(cellA2.value)
#print(cellB1.value)
#print(cellB2.value)

#print('行数',sheet.nrows)
#print('列数',sheet.ncols)

# 1列を取り出す
excelSum  = np.array( [] )
# 列の長さを追加
rows = np.array( [] )

for col in range(sheet.ncols):
   # print('--------------------------------')
    for row in range(sheet.nrows):
      #  print('(',row,':',col,')',sheet.cell(row, col).value)
        if(col == 0 and row != 0):
            # excelの1列目の値をnumpy配列に
            #rows= np.append(rows, sheet.cell(row, col).value)
            rows = np.append(rows, row)
        if(col == 1 and row != 0):
            # excelの2列目の値をnumpy配列に
            excelSum= np.append(excelSum, sheet.cell(row, col).value)


# 1列を取り出す
excelSum1  = np.array( [] )
# 列の長さを追加
rows1 = np.array( [] )
days = np.array( [] )

for col in range(sheet1.ncols):
    print('--------------------------------')
    count = 0
    for row in range(sheet1.nrows):
        if(row != 0):
            # エクセルの日付をpythonで扱えるように変換
            # excelの日付をpythonで読み込めるように変換 例: 2016-09-01 04:08:50.243000
            tstr = xlrd.xldate.xldate_as_datetime(sheet1.cell(row, col).value, book1.datemode)
            if(tstr < datetime.datetime.strptime('2016-10-01', '%Y-%m-%d')): #2016-10-01までのデータを使用する
                #print('(',row,':',col,')',xlrd.xldate.xldate_as_datetime(sheet1.cell(row, col).value, book1.datemode))
                # 例: 01 (1日のこと)
                day = tstr.strftime('%Y-%m-%d')
                days = np.append(days, datetime.datetime.strptime(day, '%Y-%m-%d'))
                # 例: 09(9月のこと)
                #print(tstr.strftime('%m'))
                # 例: 2016 9 1
                #print(tstr.year, tstr.month, tstr.day)
                #excelSum1 = np.append(excelSum1, tstr)
                rows1 = np.append(rows1, row)
                count = count + 1

# 配列の中身を計算する
words = np.array( [] )
counts = np.array( [] )
counter = Counter(days)
for word, cnt in counter.most_common():
    words = np.append(words, word)
    counts = np.append(counts, cnt)

datum = np.zeros((0,25))
datum = np.r_[datum, words.reshape(1, -1)]
datum = np.r_[datum, counts.reshape(1, -1)]
print(datum)
print(np.argsort(datum))
print(sorted(datum.items()))
#print(len(days))
#print(rows1)
#print(days)

#plt.plot(days, rows1)
#plt.plot(words, counts)
#plt.plot(datum[0], datum[1])
#plt.show()
