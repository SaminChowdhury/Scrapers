from re import sub
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
 
Requesters=[]


#Access File
driver = webdriver.Chrome(r"C:\\Users\\emeyer\\OneDrive - kean.edu\\Desktop\\Scrape\\chromedriver.exe")
driver.get("https://helpdesk.kean.edu/a/tickets/view/15000260848?order_by=created_at&order_type=desc&query_hash=%5B%7B%22value%22%3A%5B%220%22%5D%2C%22condition%22%3A%22status%22%2C%22operator%22%3A%22is_in%22%2C%22type%22%3A%22default%22%7D%2C%7B%22value%22%3A%5B%2215000283771%22%5D%2C%22condition%22%3A%22group_id%22%2C%22operator%22%3A%22is_in%22%2C%22type%22%3A%22default%22%7D%5D")
time.sleep(30)


for pages in range (100):
    numID = 1
    subID = 1
    if pages != 1:
        try:
            xPathOfButton = '//*[@id="top-pagination-next"]'
            driver.find_element("xpath", xPathOfButton).click()
            time.sleep(2)
        except:
            break
    for num in range (29):         
        #Get Name
        try:
            xPathOfProfile = '/html/body/div[3]/div[9]/div[2]/div[1]/div/div/div/div[3]/div[3]/section[2]/div[2]/div[1]/table/tbody/tr[{}]/td[4]/div/div/div[1]/div[1]/a'.format(numID)
            Name = (driver.find_element("xpath", xPathOfProfile).text)
            time.sleep(0)
            Requesters.append(Name)
            numID = numID + 1
        except:
            break
        try:
            xPathOfSubject = '/html/body/div[1]/div[9]/div[2]/div[1]/div/div/div/div[3]/div[3]/section[2]/div[2]/div[1]/table/tbody/tr[{}]/td[3]/div/a/div[1]/span[1]/text()'.format(subID)
            Subject = (driver.find_element("xpath", xPathOfSubject).text)
            time.sleep(0)
            Requesters.append(Subject)
            subID = subID + 1
        except:
            break    


 
#Export to CSV
df = pd.DataFrame({'Requester':Requesters})
df.to_csv("C:\\Users\\emeyer\\OneDrive - kean.edu\\Desktop\\Scrape\\Requesters.csv",index=False, encoding='utf-8')
driver.close()
