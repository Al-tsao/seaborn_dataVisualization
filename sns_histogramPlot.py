#載入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#數據載入
penguins = sns.load_dataset("penguins")

#繪圖
sns.set()
sns.histplot(x = "flipper_length_mm", data=penguins, color = 'r', bins = 30, edgecolor = "#FFFFFF", linewidth = 1,  label = 'aaaa') 
#color:制定bar的顏色；bins:制定有多少組數據；edgecolor:bar的邊框顏色；linewidth:bar邊框大小；label: 顯示圖表，要搭配legend()使用
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('this is a demo')
plt.legend()

#呈現
plt.show()