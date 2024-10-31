# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:11:40 2024

@author: win
"""

import requests as re
from bs4 import BeautifulSoup
import pandas as pd
def get_NowStockValue(code):
    url='https://finance.naver.com/item/main.naver?code=' +code
    html=re.get(url)
    html=html.content
    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    body=soup.find('body')
    body_table=body.select('#chart_area > div.rate_info > div > p.no_today')
    print(body_table[0].find('span').text)
    return body_table[0].find('span').text


def main():
    print('crawling-------------------------------')
    finance=list()
    a=get_NowStockValue('005930')
    finance.append(a)
    finance_tbl=pd.DataFrame(finance)
    finance_tbl.to_csv('hollys.csv', encoding='cp949', mode='w',index=True)
    
if __name__ == '__main__':
    main()