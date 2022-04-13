#載入模組
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入數據
tips = sns.load_dataset("tips")

#繪圖
sns.set()
sns.jointplot(x = tips['total_bill'], y = tips['tip'])
sns.jointplot(x = tips['total_bill'], y = tips['tip'], kind = 'hex')

#呈現
plt.show()