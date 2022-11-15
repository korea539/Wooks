# How to do Crawling / from url, requests
<br><br>

## 1. module
import pandas as pd<br>
import numpy as np<br>
import requests<br>
from bs4 import BeautifulSoup as bs<br>
import time<br>
from tqdm import trange<br>
<br>

## 2. requests url
<br>

### 1) setting url
page_no = 1<br>
url = f"https://www.mfds.go.kr/brd/m_228/list.do?page={page_no}&srchFr=&srchTo=&srchWord=&srchTp=&itm_seq_1=0&itm_seq_2=0&multi_itm_seq=0&company_cd=&company_nm="<br>
<br>

### 2) check the response and change response to html by bs(from bs4 import BeautifulSoup)
response = requests.get(url)<br>
response.text<br>
html = bs(response.text)<br>
<br>

### 3) find a route where the information i will use is included
post_no = 1<br>
title = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.center_column > a")<br>
title_str = title[0].get_text()<br>
title_split = title_str.split()<br>
<br>

part = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.center_column > div > p:nth-of-type(1)")<br>
part_str = part[0].get_text().split(" | ")[-1]<br>
<br>

view = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.center_column > div > p:nth-of-type(2)")<br>
view_str = view[0].get_text().split(" | ")[-1]<br>
view_int = int(view_str)<br>
<br>

day = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.right_column")<br>
day_str = day[0].get_text()<br>
day_date = pd.to_datetime(day_str)<br>
<br>

### 4) Contained in one list




