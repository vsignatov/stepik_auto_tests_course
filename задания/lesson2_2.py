from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
       
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    s = int(x) + int(y)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(s))
    button = browser.find_element (By.CLASS_NAME , 'btn')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
