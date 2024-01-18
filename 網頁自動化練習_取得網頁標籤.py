# 取得網頁標籤

from selenium import webdriver
import time    # 匯入時間函式

driver = webdriver.Chrome()
driver.get("https://dcard.tw/f")
print(driver.title)     # 列印網頁標籤
time.sleep(3)
# driver.quit()

