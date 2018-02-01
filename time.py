# -*- coding:utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt
def loadfile(timeLen):
    files = os.listdir(os.getcwd()+ '\\result')
    col = pd.Series({'acc_x': 0.0, 'acc_s': 0.0, 'acc_m': 0.0, 'acc_ww': 0.0})
    row = pd.Series({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0})
    file_num = 0
    for file in files:
        if file.split('_')[0] == timeLen:
            file_num = file_num + 1
            data = pd.DataFrame(pd.read_excel('result\\'+file))
            col = col + data.mean() #按列取均值
            row = row + data.mean(axis=1) #按行取均值
    print col/file_num
    print row/file_num
    return col/file_num, row/file_num
col8, row8 = loadfile('8')
col16, row16 = loadfile('16')
col26, row26 = loadfile('26')
def changeLabel(row):
    row_new = pd.Series(
        {'COVERS': 0, 'HARD DRIVES': 0, 'KEYBOARDS INTERNAL': 0, 'LCD PANELS': 0, 'LCD PARTS': 0, 'SYSTEM BOARDS': 0})
    for i in range(len(row)):
        row_new.iloc[i] = row.iloc[i]
    return row_new

plt.figure(figsize=(25, 10))
plt.subplot(211)
col8.plot(label='8_weeks')
col16.plot(label='16_weeks')
col26.plot(label='26_weeks')
plt.xlabel('Algorithm')
plt.ylabel('Accuracy')
plt.legend(loc='upper right')#, labels=['8_weeks', '16_weeks', '26_weeks'])


plt.subplot(212)
changeLabel(row8).plot(label='8_weeks')
changeLabel(row16).plot(label='16_weeks')
changeLabel(row26).plot(label='26_weeks')
plt.xlabel('PN')
plt.ylabel('Accuracy')
plt.legend(loc='upper right')
plt.show()
