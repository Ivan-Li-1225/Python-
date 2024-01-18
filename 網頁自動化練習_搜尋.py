# 自動搜尋並導頁取得網頁標籤

from selenium import webdriver
import time    # 匯入時間函式
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # 匯入使用實體鍵盤功能韓式
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www76.eyny.com/index.php")
search = driver.find_element(By.NAME,"srchtxt")
search.send_keys("求職")   # 搜尋欄輸入"求職"
search.send_keys(Keys.RETURN)   # 按Enter導頁
# WebDriverWait(driver,5).until(
#     EC.presence_of_element_located(By.XPATH, "//*[@id='scform']/tbody/tr/td[1]/h1/a/img")
# )
labels = driver.find_elements(By.CLASS_NAME,"xst")
for title in labels:
    print(title.text)



time.sleep(3)
# driver.quit()

