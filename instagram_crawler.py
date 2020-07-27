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
from import_names import import_names_and_status,verified_account


driver=webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://www.instagram.com/")
time.sleep(2)
username=driver.find_element_by_tag_name("input")
#username.send_keys("vratikajain5096")
usr="vratikajain5096"
username.send_keys(usr)
#username.send_keys(Keys.RETURN)
#pwd="paarthjain@17092001"
pwd='nakodaji12'
password=driver.find_element_by_name("password")
password.send_keys(pwd)
time.sleep(2)
login=driver.find_elements_by_tag_name("button")
login[1].click()
time.sleep(3)

try:
    driver.get("https://www.instagram.com/"+usr+"/")
    print("url done")
except:
        driver.quit()
'''buttons=driver.find_elements_by_tag_name("button")
for button in buttons:
    if button.text =="Not Now":
        print("hello")
        button.click()
time.sleep(2)'''
'''buttons2=driver.find_elements_by_tag_name("button")
for button2 in buttons2:
    if button2.text =="Not Now":
        print("hello")
        button2.click()'''
#button2=driver.find_element_by_xpath("""/html/body/div[4]/div/div/div/div[3]/button[2]""")
#button2.click()
time.sleep(3)
'''home_page=driver.page_source
soup0=BeautifulSoup(home_page,'html.parser')
profile_icon=soup0.find_all('div',{'class':'Fifk5'})
print(len(profile_icon))'''

#profile_icon=driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img""")
#profile_icon.click()

time.sleep(1)
#profile=driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]""").click()
time.sleep(6)
followers_instaname,followers_name,followers_status,following_instaname,following_name,following_status= import_names_and_status(driver)

answer=[]
for name in following_name:
    if name not in followers_name:
        answer.append(name)
print(len(answer))

normal_accounts=verified_account(driver,answer,following_instaname,following_name)
print(len(normal_accounts))

df = pd.DataFrame({'Traitorss':normal_accounts}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
driver.quit()