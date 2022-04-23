#載入模組
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入數據
tips = sns.load_dataset('tips')
print(tips)

#繪圖
sns.set()
sns.violinplot(x = 'total_bill', y = 'day', data = tips,
                hue = 'sex', split = True) #split: 如果沒有設定，那圖就會變成兩組， 男與女


#呈現
plt.show()