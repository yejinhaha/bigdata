# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:03:36 2024

@author: win
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def hollys_store(result):
    for page in range(1,10): #1~10 page
        Hollys_url ='https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
        print(Hollys_url) 
        html=urllib.request.urlopen(Hollys_url) # html 문서 받기
        soupHollys=BeautifulSoup(html, 'html.parser')
        tag_body=soupHollys.find('tbody') #tag  파싱
        for store in tag_body.find_all('tr'):
            if len(store) <= 3:
                break
            store_td=store.find_all('td')
            store_name=store_td[1].string
            store_sido=store_td[0].string
            store_address=store_td[3].string
            store_phone=store_td[5].string
            result.append([store_name]+[store_sido]+[store_address]+[store_phone])
        return
    
def main():
    result=[]
    print("crawling===================================")
    hollys_store(result)
    hollys_tbl=pd.DataFrame(result, columns=('name','sido_gu','address','phone'))
    hollys_tbl.to_csv('hollys.csv', encoding='cp949', mode='w',index=True)
    print(len(result))
    del result[:]
    
if __name__ =='__main__':
    main()    