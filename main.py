from selenium import webdriver
import time

#path = "C:/Users/Nathan/Desktop/chromedriver-win64.zip"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://www.ccisd.net/")

while(True):
    pass