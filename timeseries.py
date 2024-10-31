# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:12:17 2024

@author: win
"""

import pandas as pd
file_path="C:/Users/win/Downloads/timeseries.csv"
df=pd.read_csv(file_path)

df['new_Date']=pd.to_datetime(df['Date'])

df['Year']=df['new_Date'].dt.year
df['Month']=df['new_Date'].dt.month
df['Day']=df['new_Date'].dt.day
print(df.info())






#%%
print(df.info())
df['new_Date']=df['new_Date'].dt.to_period(freq='D')
df.set_index('new_Date',inplace=True)
print(df) 
