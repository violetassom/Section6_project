import re
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def get_closing(var):
    try:
        base_url = 'https://bizno.net'
        search_url = f"{base_url}/법인등록번호조회/?query={var}"
        page = requests.get(search_url)
        soup = BeautifulSoup(page.content,'html.parser')
        t = soup.select_one('body > section.post-area.section-gap > div > div > div.col-lg-8.post-list > div > div > div > div > a')['href']

        new_url = str(base_url+t)
        page2 = requests.get(new_url)
        soup2 = BeautifulSoup(page2.content,'html.parser')
        t2 = soup2.select_one('body > section.post-area.section-gap > div > div > div.col-lg-8.post-list > div.single-post.d-flex.flex-row > div > table.table_guide01 > tr:nth-child(9) > td').text 
        return t2
    except:
        return np.NAN

try115 = pd.read_csv('d_ent_preprocessing_ver_02.csv')
try115['폐업여부'] = ''
try115['폐업여부'] = try115['법인등록번호'].apply(get_closing)
try115.to_csv('try115(폐업여부).csv',encoding='utf-8-sig',index=False)

