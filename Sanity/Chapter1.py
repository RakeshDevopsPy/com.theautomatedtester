from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://book.theautomatedtester.co.uk/")
driver.maximize_window()
time.sleep(2)
driver.refresh()