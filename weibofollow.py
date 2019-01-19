from selenium import webdriver
import random
import os
import requests
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import re
import pdb
import time

return_value=[]
option = webdriver.ChromeOptions()
# 设置中文
#option.add_argument('headless')
#option.add_argument('--proxy-server=http://221.7.255.168:80')
from selenium import webdriver
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(3)
driver.get('https://weibo.com/')
input("please login by scan QR,then input any key")

def get_keyword_target_users(keyword_list):
    for keyword in keyword_list:
        #driver.get('https://weibo.com/5615461364/follow?from=page_100505&wvr=6&mod=headfollow#place')
        driver.get('https://s.weibo.com/')
        driver.find_element_by_xpath('//*[@id="pl_homepage_search"]/div/div[1]/a[2]').click()
        find_target_user_id_list=[]
        find_user_link_list=[]
        to_search_user_id_list=[]
        to_search_user_link_list=[]
        driver.find_element_by_xpath('//*[@id="pl_homepage_search"]/div/div[2]/div/input').send_keys(keyword)
        driver.find_element_by_xpath('//*[@id="pl_homepage_search"]/div/div[2]/button').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[2]/a').click()
        to_follow_list=[]
        find_users=[]
        find_page=0
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                user_list_html=driver.find_element_by_xpath('//*[@id="pl_user_feedList"]').get_attribute('innerHTML')
            except:
                break
            cur_users=re.findall(r'<div class="info">[\s\S]+?<a href="(.+?)" class="name"[\s\S]+?click:user_fans">(.+?)<',user_list_html)
            page=driver.find_element_by_xpath('//*[@id="pl_feed_main"]/div[1]/div[4]/div/span/a').text
            page=int(re.search(r"(\d+)",page).group(1))
            if page<find_page:
                break
            find_page=page
            for each in cur_users:
                user_link="https:"+each[0]
                fans=each[1]
                if '万' in fans:
                    fans=re.search(r"(\d+)万",fans).group(1)
                    if 100<=int(fans)<=150:
                        to_follow_list.append(user_link)
            time.sleep(1)
            next_page='not find'
            try:
                next_page=driver.find_element_by_xpath('//*[@id="pl_feed_main"]/div[1]/div[4]/div/a[2]').click()
            except:
                pass
            if next_page=='not find':
                try:
                    next_page=driver.find_element_by_xpath('//*[@id="pl_feed_main"]/div[1]/div[4]/div/a').click()
                except:
                    pass
            if next_page=='not find':
                break

        for user_link in to_follow_list:
            driver.get(user_link)
            driver.find_element_by_xpath('//*[@id="Pl_Official_Headerv6__1"]/div[1]/div/div[2]/div[4]/div/div[1]/a[1]').click()
            os.system("say 关注成功")
    driver.quit()

#keyword_list=['财经' ,'投资','投机','股票','炒股','金融','操盘','私募','公募','经济','资产','博弈','理财','证券','财富','股评','衍生品']
keyword_list=['衍生品']
get_keyword_target_users(keyword_list)
html=driver.page_source
print("finished")
driver.quit()
