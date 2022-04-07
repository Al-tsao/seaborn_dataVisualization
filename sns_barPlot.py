#載入模組
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入數據
titanic =  sns.load_dataset('titanic')
# df = sns.load_dataset('flights')
# df = df.groupby('year').sum().reset_index()

#繪圖
sns.set()
sns.barplot(x='sex', y='survived', data = titanic, hue = 'class', ci = 95)
#ci: 信心區間
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.legend()

#呈現
plt.show()