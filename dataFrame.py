# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:12:29 2024

@author: win
"""
import numpy as np
import pandas as pd
df_exam_csv=pd.read_csv('C:/Users/win/bigdata/bank/exam.csv')
df_exam_xls=pd.read_excel('C:/Users/win/bigdata/bank/exam.xlsx')
print(df_exam_csv.index)
print(df_exam_csv.columns)
df_exam_csv.info()
print(df_exam_csv.describe())
print("===============================")
print(df_exam_csv['math'].mean())
print(df_exam_csv['math'].std())
print(df_exam_csv['math'].var())


print(df_exam_csv.columns)
df1=df_exam_csv.sort_values(by='math',ascending=False).head(5)
print(df1)

df_exam_csv['total'] = df_exam_csv['english'] + df_exam_csv['math'] + df_exam_csv['science']
df_exam_csv['mean'] = (df_exam_csv['total']) / 3
df_exam_csv['test'] = np.where( df_exam_csv['mean'] >=80, 'pass', 'fail') 
#print(df_exam_csv)
#print('------------------------------------')
#print(df1.head())
#tdf=df1.head(3)
#print(tdf)
#%%
bank=pd.read_csv('C:/Users/win/bigdata/bank/bank.csv')
bank.info()

print('====================================================')
print(bank['job'].value_counts())
print(bank.describe())
en=df_exam_csv.query('english<=80')