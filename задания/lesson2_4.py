from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
       
link = "http://suninjuly.github.io/file_input.html"
a = "Иван"
b = "Иванов"
c = "test@mail.ru"
file_path = os.path.abspath(os.path.dirname('example.txt'))
    

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name=\'firstname\']')
    input1.send_keys (a)
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name=\'lastname\']')
    input2.send_keys (b)
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name=\'email\']')
    input3.send_keys (c)
    input4 = browser.find_element(By.ID, 'file')
    input4.send_keys(file_path)
    button = browser.find_element (By.CLASS_NAME, 'btn')
    button.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
