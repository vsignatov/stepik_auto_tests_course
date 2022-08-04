from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import pytest

a = "https://stepik.org/lesson/236895/step/1"
b = "https://stepik.org/lesson/236896/step/1"
c = "https://stepik.org/lesson/236897/step/1"
d = "https://stepik.org/lesson/236898/step/1"
e = "https://stepik.org/lesson/236899/step/1"
f = "https://stepik.org/lesson/236903/step/1"
g = "https://stepik.org/lesson/236904/step/1"
i = "https://stepik.org/lesson/236905/step/1"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', [a])#, b, c, d, e, f, g, i])
def test (browser, url):
    browser.get ({url})
    answer = math.log(int(time.time()))
    input1 = browser.find_element(By.ID, "ember92")
    inpit1.send_keys(answer)
    button = browser.find_element(By.CSS_NAME, "submit-submission")
    button.click()
    
    

