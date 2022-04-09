"""cat的意思是catogery，用名目尺度來分類"""

#載入模組
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入數據
tips = sns.load_dataset('tips')

#繪圖
sns.set()
# sns.catplot(x = 'day', y = 'total_bill', data = tips) #直式
# sns.catplot(x = 'total_bill', y = 'day', data = tips) #橫式
# sns.catplot(x = 'day', y = 'total_bill', data = tips, jitter = False) #jitter: 其實名目分類都是在一條線上，但是這樣會很擠，所以系統會設定稍稍左右分散
# sns.catplot(x = 'day', y = 'total_bill', data = tips, kind = 'swarm') #另一種分散方式
sns.catplot(x = 'day', y = 'total_bill', data = tips, 
            hue = 'size', kind = 'swarm', 
            order=['Sun', 'Sat', 'Fri', 'Thur']) #order: 可以改變名目順序

#呈現
plt.show()