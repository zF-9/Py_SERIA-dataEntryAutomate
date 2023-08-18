# Import Module
import pandas as pd 
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

# open browser - chrome req: ver 114
driver = webdriver.Firefox()

#import csv to panda table
dataframe = pd.read_csv('SENARAI.PERUNDANGAN.csv', usecols=['AGENSI_xn', 'name'])
dataframe.columns = ['AGENCY', 'Ordinance']


#dataframe = df.iloc[1: , :]
print(dataframe)

# Open URL
###driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf-F-_UeA8AAxfFN6_yOQgi3rgakm0lZiLTMAGEfqJCfp-2hA/viewform?usp=sf_link')
driver.get('http://localhost:8000/login')

# wait for one second, until page gets fully loaded
time.sleep(3)

#login creds

no_ic = '880621125761'
pswd = 'wasd'


ic = driver.find_element("xpath", '//*[@id="input-10"]')
ic.send_keys(no_ic)
password = driver.find_element("xpath", '//*[@id="input-13"]')
password.send_keys(pswd)

time.sleep(1)

#attempt login 
login_btn = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/form/div[3]/div/button')
login_btn.click()

time.sleep(1)

#navigate to admin panel after login 
admin_panel = driver.find_element("xpath", '/html/body/div[1]/div/header/div/div[2]/button[3]')
admin_panel.click()


time.sleep(1)

#navigate to perundagan entry form 
perundangan_btn = driver.find_element("xpath", '/html/body/div[1]/div/main/div/div/div/ul[2]/li[4]')
perundangan_btn.click()

time.sleep(1)

tambah_perundangan = driver.find_element("xpath", '/html/body/div[1]/div/main/div/div/div/div[1]/div[2]/button')
tambah_perundangan.click()

time.sleep(1)

for data in dataframe:
    count = 0 
    time.sleep(2)
    print(data)
    #print(data_lawname)
    
    #click to show dropdown
    dropMenu = driver.find_element("xpath", '/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div')
    dropMenu.click()

    #fill in the field 
    org_berkaitan = driver.find_element("xpath", '//*[@id="input-159"]')
    #org_berkaitan.send_keys('Jabatan Arkib Negeri Sabah')
    #org_berkaitan.send_keys(data_agensi)

    law_name = driver.find_element("xpath", '//*[@id="input-164"]') 
    #contoh_perundangan = 'testing akta 1994'
    #law_name.send_keys(contoh_perundangan)
    #law_name.send_keys(data_agensi)

    count +1

    #refresh webdiriver
    #driver.refresh()
    #time.sleep(2)



