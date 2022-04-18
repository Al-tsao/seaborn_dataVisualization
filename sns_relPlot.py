"""relplot，是relation plot的意思，使用這個方法可以繪製scatter plot和line plot，至於為何不使用scatterplot
和lineplot，因為不能有子圖集
Ref: https://ppfocus.com/0/di117f24c.html"""

#載入模組
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入數據
#scatterplot
tips = sns.load_dataset("tips")
#lineplot
fmri = sns.load_dataset("fmri")


#繪圖
sns.set()
#scatterplot
sns.relplot(data=tips, x="total_bill", y="tip", hue="day", col="time", row="sex")
#lineplot
sns.relplot(data=fmri, x="timepoint", y="signal", col="region", kind="line", ci = 99) #ci: 信心區間的大小

#呈現
plt.show()