# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:44:24 2024

@author: win
"""

import pandas as pd
from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

file_path="C:/Users/win/Downloads/time_series2.csv"
df=pd.read_csv(file_path)
print(df.info())
df['new_Date']=pd.to_datetime(df['date'])
df.set_index('new_Date',inplace=True)

plt.rcParams.update({'figure.figsize':(10,7), 'figure.dpi':120})

def plot_df(df,x,y,title="", xlabel='date',ylabel='value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x,y,color='tab:red')
    plt.gca().set(title=title,xlabel=xlabel,ylabel=ylabel)
    plt.show()
    
plot_df(df, x=df.date, y=df.value, title="Time series data")