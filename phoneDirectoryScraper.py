
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
fName=[] 
lName=[] 
dName=[]
pNumber=[]
eAddress=[]

driver.get('https://directory.kean.edu/')
button = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div[1]/label/select')
button.click()
button1 = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div[1]/label/select/option[4]')
button1.click()

for i in range(23):  
    if i != 0 and i != 22:
        button2 = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[2]/span[4]')
        button2.click()
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")
    for a in soup.findAll(attrs={'odd'}):
        name = a.find_all('td')
        if name[0].text in fName and name[1].text in lName and name[5].text in eAddress:
            break
        eAddress.append(name[5].text)
        fName.append(name[0].text)
        lName.append(name[1].text)
        dName.append(name[2].text)
        pNumber.append(name[3].text)
        
   
    for a in soup.findAll(attrs={'even'}):
        name = a.find_all('td')
        if name[0].text in fName and name[1].text in lName and name[5].text in eAddress:
            break
        eAddress.append(name[5].text)
        fName.append(name[0].text)
        lName.append(name[1].text)
        dName.append(name[2].text)
        pNumber.append(name[3].text)
        
   
    time.sleep(0.5)

driver.quit()

df = pd.DataFrame({'First Name':fName,'Last Name':lName,'Department Name':dName, 'Phone Number':pNumber, 'Email Address':eAddress}) 
df.to_csv('directory.csv', index=False, encoding='utf-8')
