from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import re
import pdb
import time

return_value=[]
def get_one_page_values(html):
    table_data=re.search(r'<table id="main-table" class="dataTable no-footer" role="grid">(.+)</table>',html).group(1)
    onepage_items=re.findall(r'<tr role="row" class=[^<>]+>.+?</tr>',table_data)
    one_page_values=[]
    for item in onepage_items:
        _=re.search(r"(\d+)</a>.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<.+?>([^\s<>]+?)<",item)
        return_item=[]
        return_item.append(_[1])
        return_item.append(_[9])
        return_item.append(_[10])
        one_page_values.append(return_item)
    return one_page_values

option = webdriver.ChromeOptions()
#option.add_argument('headless')
#option.add_argument('--proxy-server=http://221.7.255.168:80')
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(10)
driver.get('http://quote.eastmoney.com/center/gridlist.html#options_sh50etf_all')
html=driver.page_source
page_wanted_values=get_one_page_values(html)
return_value.append(page_wanted_values)
pagenum=1
halttimes=0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    e=driver.find_element_by_id('main-table_next')
    time.sleep(3)
    e.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
    pagenum+=1
    print(pagenum)
    html=driver.page_source
    page_wanted_values=get_one_page_values(html)
    if page_wanted_values in return_value:
        halttimes+=1
        if halttimes<3:
            continue
        else:
            break
    else:
        return_value.append(page_wanted_values)
driver.quit()
if os.path.exists("qiquan_result.txt"):
    os.system("rm qiquan_result.txt")
with open("qiquan_result.txt","a+") as f:
    for each in return_value:
        for _ in each:
            f.write(_[0]+"    "+_[1]+"    "+_[2]+"\r\n")

