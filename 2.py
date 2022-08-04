from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

browser = webdriver.Chrome()
browser.get ("https://stepik.org/lesson/236895/step/1")
time.sleep (5)
answer = math.log(int(time.time()))
input1 = browser.find_element(By.ID, "ember87")
input1.send_keys(answer)
button = browser.find_element(By.CLASS_NAME, "submit-submission")
button.click()
time.sleep (2)
message = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
print (message)
