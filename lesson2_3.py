from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
       
link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value').text
    x = calc(int(x_element))
    input1 = browser.find_element (By.ID, 'answer')
    input1.send_keys(x)
    browser.execute_script("window.scrollBy(0, 100);")
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
