# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:17:37 2024

@author: win
"""

import numpy as np
import pandas as pd
city=['인천','부산','대구','대전','광주']
hollys_csv=pd.read_csv('C:/Users/win/bigdata/bank/hollys.csv', encoding='cp949')
print(hollys_csv.columns)

si=list()
for i in hollys_csv['sido-gu']:
    d=i.split( )[0]
    si.append(d)
    
hollys_csv['sido'] = si

hollys2_df=hollys_csv.query('sido in @city')
print(hollys2_df.columns)
res1=hollys2_df['sido'].value_counts()

hollys2_df['sido'] = pd.Categorical(hollys2_df['sido'], categories=city, ordered=True)
hollys2_df = hollys2_df.sort_values(by='sido')
print(hollys2_df.info())