# -*- coding:utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt
def loadfile(timeLen):
    files = os.listdir(os.getcwd()+ '\\result')
    file_num = 0
    for file in files:
        if file.split('_')[0] == timeLen:
            file_num = file_num + 1
            if file_num == 1:
                data = pd.DataFrame(pd.read_excel('result\\'+file))
            else:
                data = data + pd.DataFrame(pd.read_excel('result\\'+file))
    new_label = ['COVERS', 'HARD DRIVES', 'KEYBOARDS INTERNAL', 'LCD PANELS', 'LCD PARTS', 'SYSTEM BOARDS']
    data.index = new_label
    col_label = ['acc_x', 'acc_s', 'acc_m', 'acc_ww']
    for i, i1 in zip(new_label, range(len(new_label))):
        for j, j1 in zip(col_label, range(1, len(col_label) + 1)):
            data.set_value(i, j, data.values[i1][j1] / file_num)
    return data
data8 = loadfile('8')
data16 = loadfile('16')
data26 = loadfile('26')
fig = plt.figure(figsize=(25, 10))

ax11 = fig.add_subplot(211)
ax12 = fig.add_subplot(223)
ax13 = fig.add_subplot(224)
data8.plot(ax=ax11, title='8_Weeks')
data16.plot(ax=ax12, title='16_Weeks')
data26.plot(ax=ax13, title='26_Weeks')
plt.show()