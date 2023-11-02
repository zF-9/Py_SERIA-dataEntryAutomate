# Import Module
import pandas as pd 
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

# open browser - chrome req: ver 114
driver = webdriver.Firefox()

#import csv to panda table
dataframe = pd.read_csv('SENARAI-PERUNDANGAN_verify.csv', usecols=['AGENSI_xn', 'name'])
dataframe.columns = ['AGENCY', 'Ordinance']


#dataframe = df.iloc[1: , :]
print(dataframe)

# Open URL
# driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf-F-_UeA8AAxfFN6_yOQgi3rgakm0lZiLTMAGEfqJCfp-2hA/viewform?usp=sf_link')
# driver.get('http://localhost:8000/login') # test on local server 
driver.get('https://seria.digitalsabah.gov.my/login')

# wait for one second, until page gets fully loaded
time.sleep(3)

#login creds
no_ic = '880621125761'
pswd = '#'


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

row_count = range(dataframe.shape[0])

for data in row_count:
    driver.refresh()
    time.sleep(2)
    #print(dataframe.iloc[count])
    #print(data_lawname)
    
    #click to show dropdown
    dropMenu = driver.find_element("xpath", '/html/body/div[1]/div[1]/main/div/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div')
    dropMenu.click()

    #fill in the field 
    org_berkaitan = driver.find_element("xpath", '//*[@id="input-37"]') 
    orgs_ = dataframe['AGENCY'].iloc[data]
    print(orgs_)
    org_berkaitan.send_keys(orgs_)
    
    #org_berkaitan.send_keys('Jabatan Arkib Negeri Sabah')
    #org_berkaitan.send_keys(data_agensi)
    
    selectClick = driver.find_element("xpath", '/html/body/div/div[2]/div/div/div/div')
    selectClick.click()

    law_name = driver.find_element("xpath", '//*[@id="input-42"]')
    laws_ = dataframe['Ordinance'].iloc[data]
    print(laws_)
    law_name.send_keys(laws_)
    
    #contoh_perundangan = 'testing akta 1994'
    #law_name.send_keys(contoh_perundangan)
    #law_name.send_keys(data_agensi)

    #refresh webdiriver
    #driver.refresh()
    time.sleep(7)

    #click simpan button
    insert = driver.find_element("xpath", '/html/body/div/div[1]/main/div/div/div/div[2]/div/div/div/form/div[2]/div/button')
    insert.click()
    time.sleep(7)
    
    #errMsgs_ = driver.find_element("xpath", '/html/body/div/div[1]/main/div/div/div/div[3]/div/div/div/form/div[1]/div/div[3]/div/div/div/div[2]/div/div/div')
    #succMsgs_ = driver.find_element("xpath", '/html/body/div/div[1]/main/div/div/div/div[2]/div/div')

    # whatNotPunyaMessage_example = driver.find_element("xpath", "//*[contains(text(),'someUniqueString')]") 
    
    if driver.find_element("xpath", '/html/body/div/div[1]/main/div/div/div/div[2]/div/div').text == "Maklumat berjaya disimpan" : #succMsgs_ == 'Maklumat berjaya disimpan' :
        print('New entry added!')
        time.sleep(9)
        driver.refresh()
        

    elif driver.find_element("xpath", '/html/body/div/div[1]/main/div/div/div/div[2]/div/div').text == "Sila semak semula maklumat anda" :
        print('Nothing new was added!')
        time.sleep(9)
        driver.refresh()

    else:
        time.sleep(2)
        driver.refresh()
        

    



