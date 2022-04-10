#載入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#數據載入
df = sns.load_dataset('flights')
df  = df.pivot(index = 'month',columns = 'year',values = 'passengers')

#繪圖
sns.set()
heatmap = sns.heatmap(df, cmap = 'rocket_r') #cmap:制定熱力圖顏色
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation = 30) #繪製x軸標示角度
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation = 0) #繪製y軸標示角度
plt.xlabel('Year')
plt.ylabel('Month')
plt.title('this is a demo')

#呈現
plt.show()