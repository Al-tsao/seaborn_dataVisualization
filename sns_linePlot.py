#載入模組
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#數據載入
fmri = sns.load_dataset("fmri")

#繪圖
sns.set()
sns.lineplot(x = 'timepoint', y = 'signal', style = 'event', hue = 'region', data = fmri, markers = True, ci = 95, err_style = 'bars') #ci: 信心區間的大小

#呈現
plt.show()