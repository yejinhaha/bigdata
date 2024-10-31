# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:20:30 2024

@author: win
"""

import pandas as pd
import numpy as np
from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

file_path="C:/Users/win/Downloads/time_series2.csv"
df=pd.read_csv(file_path, parse_dates=['date'], index_col='date')
df.reset_index(inplace=True)
print(df.info())
df['year']=[d.year for d in df.date ]
df['month']=[d.strftime('%b') for d in df.date]

years=df['year'].unique()
np.random.seed(100)
mycolors=np.random.choice(list(mpl.colors.XKCD_COLORS.key()), len(years),replace=False)
plt.figure(figsize=(16,12), dpi=80)
for i,y in enumerate(years):
    if i>0:
        plt.plot('month','value',data=df.loc[df.year == y,:],
        color=mycolors[i], label=y)
        plt.text(df.loc[df.year==y,:].shape[0]-.9, df.loc[df.year==y, 'value'][-1:].values[0], y, fontsize=12, color=mycolors[i])
        
plt.show()