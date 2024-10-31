# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:08:56 2024

@author: win
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
url="https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=005930"
#urllib.reauests기능 유사
driver=webdriver.Chrome()
driver.get(url)

html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
table=soup.select('table')
table_html=str(table)
tabe_df_list=pd.read_html(table_html)

#%%
fs=tabe_df_list[12]
fs.set_index(('주요재무정보','주요재무정보'), inplace=True)
fs.index.rename('주요재무정보', inplace=True)
fs.columns=fs.columns.droplevel(0)
fs.to_csv('dynamic.csv', encoding='cp949', mode='w', index=True)
driver.close()