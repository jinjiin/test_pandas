# -*- coding:utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt
def loadfile(timeLen):
    files = os.listdir(os.getcwd()+ '\\result')
    file_num = 0
    for file in files:
        if file.split('_')[3] == timeLen + '.xlsx':
            file_num = file_num + 1
            if file_num == 1:
                data = pd.DataFrame(pd.read_excel('result\\'+file))
            else:
                data = data + pd.DataFrame(pd.read_excel('result\\'+file))
    new_label = ['COVERS', 'HARD DRIVES', 'KEYBOARDS INTERNAL', 'LCD PANELS', 'LCD PARTS', 'SYSTEM BOARDS']
    data.index = new_label
    col_label = ['acc_x', 'acc_s', 'acc_m', 'acc_ww']
    for i, i1 in zip(new_label, range(len(new_label))):
        for j, j1 in zip(col_label, range(1, len(col_label)+1)):
            data.set_value(i, j, data.values[i1][j1]/file_num)
    return data
data_201609 = loadfile('201609')

data_201611 = loadfile('201611')
data_201701 = loadfile('201701')
data_201703 = loadfile('201703')
data_201705 = loadfile('201705')
#f, axes = plt.subplots(2, 3, figsize=(10, 8))
fig = plt.figure(figsize=(25, 10))

ax11 = fig.add_subplot(221)
ax12 = fig.add_subplot(222)
ax13 = fig.add_subplot(223)
ax14 = fig.add_subplot(224)

data_201609.plot(ax=ax11, title='Until 201609')
data_201611.plot(ax=ax12, title='Until 201611')
data_201701.plot(ax=ax13, title='Until 201701')
data_201703.plot(ax=ax14, title='Until 201703')

plt.show()

data_201705.plot(title='Until 201705')
plt.show()