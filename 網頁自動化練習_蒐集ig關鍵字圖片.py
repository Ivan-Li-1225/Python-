from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:/Users/ahc60/Downloads/chromedriver-win64/chromedriver-win46/chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")
username = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "username"))
    )
password = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "password"))
    )
login = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
username.clear()
password.clear()
username.send_keys("ahc3000@gmail.com")
time.sleep(1)
password.send_keys("Koe1050259")
time.sleep(1)
login.click()

search = driver.find_element(By.CSS_SELECTOR, "#mount_0_0_Er > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk > div > div > div.xopu45v.xu3j5b3.xm81vs4.x1vjfegm > div > div.x1iyjqo2.xh8yej3 > div:nth-child(2) > span > div > a > div > div > div > div > svg > path")
search.click()

# websearch = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, ""))
#     )
# keyword = "#cat"
# websearch.send_keys(keyword)
# time.sleep(1)
# websearch.send_keys(Keys.RETURN)
# time.sleep(1)
# websearch.send_keys(Keys.RETURN)


time.sleep(5)   # 等待5秒關閉網頁
