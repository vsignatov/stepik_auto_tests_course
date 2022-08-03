import math
from selenium import webdriver
from selenium.webdriver.common.by import By

host = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(host)
text_seach_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element(By.LINK_TEXT, text_seach_link)
link.click ()

try:
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CLASS_NAME, 'btn-default')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
