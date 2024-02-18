from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

#path = "C:/Users/Nathan/Desktop/chromedriver-win64.zip"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://www.ticketmaster.com/")

running = True

while(running):
    search = driver.find_element(By.ID, 'searchFormInput-input')
    search.send_keys("Taylor Swift")
    search.send_keys(Keys.RETURN)
    time.sleep(10)

    running = False

else:
    driver.quit()