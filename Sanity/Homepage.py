from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://book.theautomatedtester.co.uk/")
driver.page_source.find("Selenium: Beginners Guide")
page_title=driver.title
if page_title == "Selenium: Beginners Guide" :
    print(page_title)
else:
    print("title of the page mismatched")
for a in driver.find_elements_by_tag_name('a'):
    print(a.get_attribute('href'))
driver.close()