import selenium
from selenium import webdriver
driver=webdriver.Chrome('chromedriver.exe')
import time

time.sleep(1)

driver=webdriver.Chrome('chromedriver.exe')
driver.get('http://www.naver.com')

from selenium.webdriver.common.by import By

elem=driver.find_element(By.XPATH, '//*[@id="q"]')
elem.send_keys("시청률")

# 클릭 
elem1=driver.find_element(By.XPATH, '//*[@id="nx_search_form"]/fieldset/button')
elem1.click()

# 일일 시청률 입력
elem2=driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div/div[2]/div[2]/div[1]/ul/li[1]')
elem2.click()

# text오브젝트를 추가하고 이를 변수에 할당

wrate_text=driver.find_element(By.XPATH, '//*[@id="jupTvRatingColl"]/div[2]/div[1]/div[3]/div/table/tbody').text

#1
print(wrate_text) 
    
tmp=[i.split() for i in wrate_text.split('\n')]

#2
print(tmp)
print()

tmp_1=[tmp[i]+tmp[i+1] for i in range(0, len(tmp),2)]

#3
print(tmp_1)
print()

# TV프로그램이 단어별로 분리 되어 있으므로 이를 합치는 코드를 다음과 같이 작성
tmp_list=[[tmp_1[i][0]," ".join(tmp_1[i][1:-2]), tmp_1[i][-2],tmp_1[i][-1]] for i in range(len(tmp_1))]

#4
print(tmp_list)
print()

import pandas as pd

df=pd.DataFrame.from_records(tmp_list, columns=['순위','프로그램명','채널','시청률'])
#5
print(df)