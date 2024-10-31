# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:49:33 2024

@author: win
"""

import pandas as pd
import matplotlib.pyplot as plt


file_path="C:/Users/win/Downloads/pusan_pop(1).csv"
df_pusan=pd.read_csv(file_path, encoding='cp949')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False



pusan = df_pusan.loc[ :, ['region','총인구']]

import numpy as np
ratio = pusan.총인구
labels = pusan.region

cmap=plt.get_cmap('viridis')

colors=cmap(np.linspace(0,1,len(labels)))

plt.pie(ratio,labels=labels, autopct="%.1f%%", colors=colors)



plt.show()