import xlrd
import numpy as np
import matplotlib.pyplot as plt

# 1列を取り出す
excelSum  = np.array( [] )
# 列の長さを追加
rows = np.array( [] )

# Excelファイル読み込み
book = xlrd.open_workbook("pythonTest2.xlsx")
sheet1 = book.sheet_by_index(0)

cellA1 = sheet1.cell(0, 0)
cellA2 = sheet1.cell(1, 0)
cellB1 = sheet1.cell(0, 1)
cellB2 = sheet1.cell(1, 1)

print(cellA1.value)
print(cellA2.value)
print(cellB1.value)
print(cellB2.value)

print('行数',sheet1.nrows)
print('列数',sheet1.ncols)

for col in range(sheet1.ncols):
    print('--------------------------------')
    for row in range(sheet1.nrows):
        print('(',row,':',col,')',sheet1.cell(row, col).value)
        if(col == 0 and row != 0):
            # excelの1列目の値をnumpy配列に
            #rows= np.append(rows, sheet1.cell(row, col).value)
            rows = np.append(rows, row)
        if(col == 1 and row != 0):
            # excelの2列目の値をnumpy配列に
            excelSum= np.append(excelSum, sheet1.cell(row, col).value)

print(rows)
print(excelSum)

plt.plot(rows, excelSum)
plt.show()
