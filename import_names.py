from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select 
def import_names_and_status(driver):
    ul=driver.find_element_by_tag_name("ul") #to click on followers...this <ul> is the first one in the source code
    li=ul.find_elements_by_tag_name("li")
    number_of_followers=0
    for item in li:
        if "followers" in item.text:
            number_of_followers=int(item.text.split(" ")[0])
            item.click()
    time.sleep(3)
    followers_window=driver.find_element_by_xpath("""/html/body/div[4]/div/div/div[2]""")
    #class_names=driver.find_element_by_xpath("""/html/body/div[4]/div/div/div[2]/ul""")
    #names=class_names.find_elements_by_tag_name("li")
    for i in range(int(number_of_followers/5)):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_window)
            time.sleep(random.randint(500,1000)/1000)
            
    followers_page=driver.page_source
    soup=BeautifulSoup(followers_page,'html.parser')
    #followers_name=soup.find_all('a',{'class':'FPmhX notranslate  _0imsa '})
    followers_instaname_element=soup.find_all('div',{'class':'d7ByH'})
    print(len(followers_instaname_element))
    followers_instaname=[]
    for name in followers_instaname_element:
        followers_instaname.append(name.text)

    followers_name_element=soup.find_all('div',{'class':'wFPL8'})
    print(len(followers_name_element))
    followers_name=[]
    for name in followers_name_element:
        followers_name.append(name.text)

    followers_status_element=soup.find_all('div',{'class':'Pkbci'})
    print(len(followers_status_element))
    followers_status=[]
    for name in followers_status_element:
        followers_status.append(name.text)

    driver.back()

    ul=driver.find_element_by_tag_name("ul") #to click on followers...this <ul> is the first one in the source code
    li=ul.find_elements_by_tag_name("li")
    number_of_following=0
    for item in li:
        if "following" in item.text:
            number_of_following=int(item.text.split(" ")[0])
            item.click()
    time.sleep(1)
    following_window=driver.find_element_by_xpath("""/html/body/div[4]/div/div/div[2]""")
    for i in range(int(number_of_following/5)):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_window)
            time.sleep(random.randint(500,1000)/1000)
            
    following_page=driver.page_source
    soup2=BeautifulSoup(following_page,'html.parser')
    #followers_name=soup.find_all('a',{'class':'FPmhX notranslate  _0imsa '})
    following_instaname_element=soup2.find_all('a',{'class':'FPmhX notranslate _0imsa'})
    print(len(following_instaname_element))
    following_instaname=[]
    for name in following_instaname_element:
        following_instaname.append(name.text)

    #following_name_element=soup2.find_all('div',{'id':'f3f95738117768c'})
    following_name_element=soup2.find_all('div',{'class':'wFPL8'})
    print(len(following_name_element))
    following_name=[]
    for name in following_name_element:
        following_name.append(name.text)

    following_status_element=soup2.find_all('button',{'class':'sqdOP L3NKy _8A5w5'})
    print(len(following_status_element))
    following_status=[]
    for name in following_status_element:
        following_status.append(name.text)
    return followers_instaname,followers_name,followers_status,following_instaname,following_name,following_status
def verified_account(driver,answer,following_instaname,following_name):
    answer_final=[]
    for name in answer:
        #print(name)
        index=following_name.index(name)
        insta_name=following_instaname[index]
        #print(insta_name)
        
        try:
            driver.get("https://www.instagram.com/"+insta_name+"/")
            time.sleep(1)
            verify = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span"""))
            )
            no_of_followers=verify.text.split(" ")[0]
            if no_of_followers[-1]=='m':
                no_of_followers=int(no_of_followers.slice(0,-1))*1000000
            elif(no_of_followers[-1]=='k'):
                no_of_followers=int(no_of_followers.slice(0,-1))*1000
            else:
                no_of_followers=int(no_of_followers)
            if no_of_followers<2000:
                answer_final.append(name)
                print(name)
        except:
            print(" ")
            #print("account is not verfied")
            #driver.quit()
    #answer_final=[x for x in answer if x not in verified_names]
    return answer