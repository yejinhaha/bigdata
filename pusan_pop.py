# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:36:13 2024

@author: win
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

file_path="C:/Users/win/Downloads/pusan_pop.csv"
df = pd.read_csv(file_path, encoding='cp949')
print(df.info())
pusan = df.loc[:,['region', '총인구']]

pusan.plot(x='region',y='총인구', color='dodgerblue')
plt.show()

plt.rcParams['figure.figsize'] = (7,6)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False