# 網頁功能操作

from selenium import webdriver
import time    # 匯入時間函式
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # 匯入使用實體鍵盤功能韓式
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www76.eyny.com/index.php")
search = driver.find_element(By.NAME,"srchtxt")
search.clear()   # 清除欄位預設文字
search.send_keys("求職")
search.send_keys(Keys.RETURN)
# WebDriverWait(driver,5).until(
#     EC.presence_of_element_located(By.XPATH, "//*[@id='scform']/tbody/tr/td[1]/h1/a/img")
# )
# labels = driver.find_elements(By.CLASS_NAME,"xst")
# for title in labels:
#     print(title.text)

links = driver.find_element(By.XPATH, "//*[@id='462606']/tr/th/a")   # 點擊標籤"錢多事少離家近？新鮮人求職最重這點"
links.click()   # 點擊該標籤並導頁
# driver.back()   # 返回上一頁
# driver.forward()   # 返回下一頁

time.sleep(5)
# driver.quit()

