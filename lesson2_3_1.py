from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
       
link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    img = browser.find_element(By.ID, 'input_value').text
    x = int(img)
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button1 = browser.find_element(By.CLASS_NAME, 'btn')
    button1.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
