from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
       
link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    img = browser.find_element(By.ID, 'treasure')
    x = img.get_attribute ("valuex")
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys (y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option1.click()
    button = browser.find_element(By.CLASS_NAME, 'btn-default')
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
