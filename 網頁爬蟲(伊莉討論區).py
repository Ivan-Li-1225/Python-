# https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# from selenium.webdriver import Keys

PATH = "C:/Users/ahc60/Downloads/chromedriver-win64/chromedriver-win46/chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www76.eyny.com/index.php")
search = driver.find_element(By.NAME,"srchtxt")
search.clear()     # 輸入欄位清空
time.sleep(1)
search.send_keys("求職")
time.sleep(1)
search.send_keys(Keys.RETURN)
# WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "nvhm"))
# )
driver.back()
titles = driver.find_elements(By.CLASS_NAME,'grouplist')
for title in titles:
    print(title.text)

time.sleep(5)   # 等待3秒
driver.quit()   # 關閉頁面