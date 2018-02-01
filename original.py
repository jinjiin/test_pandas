# -*- coding:utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt
def loadfile(timeLen):
    files = os.listdir(os.getcwd()+ '\\result')
    fig = plt.figure(figsize=(25, 10))
    fig.set_label(timeLen)
    file_num = 0
    for file in files:
        if file.split('_')[3] == timeLen + '.xlsx':
            file_num = file_num + 1
            data = pd.DataFrame(pd.read_excel('result\\' + file))
            new_label = ['COVERS', 'HARD DRIVES', 'KEYBOARDS INTERNAL', 'LCD PANELS', 'LCD PARTS', 'SYSTEM BOARDS']
            data.index = new_label
            ax11 = fig.add_subplot(2, 2, file_num)
            data.plot(ax=ax11, title= file.split('_')[0] + ' Weeks')
    plt.show()

loadfile('201705')