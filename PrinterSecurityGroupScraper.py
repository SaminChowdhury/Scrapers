from re import sub
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from bs4 import BeautifulSoup
import pandas as pd
import time
 
PrinterName=[]
printGroupName=[]
 
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
 
#Access File
driver = webdriver.Chrome('chromedriver')
driver.get("C:\\Users\\schowd\\Desktop\\SCrape\\final.htm")
time.sleep(1)
 
#Expand file
driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[2]/div').click()
time.sleep(2)
 
#Hide All
#driver.find_element("xpath", '/html/body/table/tbody/tr[2]/td[2]/div').click()
 
#Open Find Bar
#pyautogui.hotkey('ctrl', 'f')
 
#Forloop for Printer Names
for num in range (417):
    if num%2!=0: #For Printer Names
        xpathOfName = '/html/body/div[7]/div[2]/div[2]/div[2]/div[{}]/span'.format(num)
        Pname = (driver.find_element("xpath",xpathOfName).text)
        PnameLength = (len(Pname))
        PrinterName.append(Pname[33:PnameLength-1])
    if num%2==0 and num != 0: #For Group Names
        if num != 274 and num != 282: #Excluding printer Names with no group
            xpathOfGroup ='/html/body/div[7]/div[2]/div[2]/div[2]/div[{}]/div[2]/div[4]/div/table[2]/tbody/tr[4]/td[2]'.format(num)
            Gname = (driver.find_element("xpath",xpathOfGroup).text)
            GnameLength = (len(Gname))
            printGroupName.append(Gname[12:GnameLength])      
        else:
            printGroupName.append("No Group")
#Scroll Down To Bottom of Page
    if num == 270:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
 
#Export to CSV
df = pd.DataFrame({'Printer Name':PrinterName,'Printer Group':printGroupName})
df.to_csv('test.csv',index=False, encoding='utf-8')
