#載入模組
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入數據
tips = sns.load_dataset("tips")

#繪圖
sns.set()
sns.pairplot(tips)

#呈現
plt.show()