import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver
driver = webdriver.Chrome()

# Url open
driver.get("https://www.google.com")
driver.maximize_window()

# Searching on Google
textarea = driver.find_element(By.NAME, "q")        #i think find_element_by_name was in older version 
textarea.send_keys("Selenium")
time.sleep(2)
textarea.send_keys(Keys.RETURN)            ## button = driver.find_element(By.NAME, "btnK")         #giving error ---  selenium.common.exceptions.ElementNotInteractableException
                                            # button.click()
# Going back on webpage
time.sleep(3)
driver.back()

#Now going to amazon
driver.get("https://www.amazon.com")
time.sleep(3)

driver.find_element(By.CLASS_NAME, "a-button-input").click()

# Selecting links
driver.find_element(By.LINK_TEXT, "Today's Deals").click()
time.sleep(3)

driver.refresh()        #Refresh the page

driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("Gaming Laptop")
time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]').click()
time.sleep(2)

# Getting Data
items = driver.find_elements(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]')

total = len(items)
print(str(total)+ " items found")

i=total-1
for item in items:
    j = total-i
    print(f"Item No.{j} - {item.text[:50]}")
    i -=1
time.sleep(5)
driver.quit()