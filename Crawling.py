# Module
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import time
from tqdm import trange


# setting url
page_no = 1
url = f"https://www.mfds.go.kr/brd/m_228/list.do?page={page_no}&srchFr=&srchTo=&srchWord=&srchTp=&itm_seq_1=0&itm_seq_2=0&multi_itm_seq=0&company_cd=&company_nm="


# check the response and change response to html by bs(from bs4 import BeautifulSoup)
response = requests.get(url)
response.text
html = bs(response.text)


# find a route where the information i will use is included
post_no = 1
title = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.center_column > a")
title_str = title[0].get_text()
title_split = title_str.split()

part = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.center_column > div > p:nth-of-type(1)")
part_str = part[0].get_text().split(" | ")[-1]

view = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.center_column > div > p:nth-of-type(2)")
view_str = view[0].get_text().split(" | ")[-1]
view_int = int(view_str)

day = html.select(f"#content > div.bbs_list01 > ul > li:nth-of-type({post_no}) > div.right_column")
day_str = day[0].get_text()
day_date = pd.to_datetime(day_str)


# Contained in one list
