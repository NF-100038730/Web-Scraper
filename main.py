from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

#path = "C:/Users/Nathan/Desktop/chromedriver-win64.zip"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def checkShows(location, date, artist):
    driver.get("https://www.ticketmaster.com/")
    time.sleep(2.5)
    locationSearch = driver.find_element(By.CLASS_NAME, 'sc-ttovyh-2 hgNgbE')
    locationSearch.send_keys(location)
    time.sleep(2.5)
    #dateSearch = driver.find_element()
    #dateSearch.send_keys(date)
    time.sleep(2.5)
    artistSearch = driver.find_element(By.ID, 'searchFormInput-input')
    artistSearch.send_keys(artist)
    artistSearch.send_keys(Keys.RETURN)

# time.sleep(60)

# concertInfo = input("Enter city (eg. 77002, Houston, TX) >> "), input("Enter date (eg. 01/01/2024) >> "), input("Enter artist (eg. Taylor Swift) >> ")

# locationSearch = driver.find_element(By.CLASS_NAME, 'sc-ttovyh-2 hgNgbE')
# locationSearch.send_keys(concertInfo[0])
# #dateSearch = 
# artistSearch = driver.find_element(By.ID, 'searchFormInput-input')
# artistSearch.send_keys(concertInfo[2])
# artistSearch.send_keys(Keys.RETURN)

# time.sleep(10)

# running = False

# driver.quit()