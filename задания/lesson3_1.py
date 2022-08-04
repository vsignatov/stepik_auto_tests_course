from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class test_site (unittest.TestCase):
	def test_fun_1 (self):
		try:
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)
			# Заполнение формы данными
			input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class .first')
			input1.send_keys("first_name")
			input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
			input1.send_keys("last_name")
			input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class .third')
			input1.send_keys("email")
			# нажаьте на кнопку отправить
			button = browser.find_element(By.CLASS_NAME, "btn")
			button.click()
			# находим элемент, содержащий текст
			welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
			# записываем в переменную welcome_text текст из элемента welcome_text_elt
			welcome_text = welcome_text_elt.text
			# проверяем правильность полученного текста
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
		finally:
			time.sleep(5)
			browser.quit()
			
	def test_fun_2 (self):
		try:
			link = "http://suninjuly.github.io/registration2.html"
			browser = webdriver.Chrome()
			browser.get(link)
			# Заполнение формы данными
			input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class .first')
			input1.send_keys("first_name")
			input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
			input1.send_keys("last_name")
			input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class .third')
			input1.send_keys("email")
			# нажаьте на кнопку отправить
			button = browser.find_element(By.CLASS_NAME, "btn")
			button.click()
			# находим элемент, содержащий текст
			welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
			# записываем в переменную welcome_text текст из элемента welcome_text_elt
			welcome_text = welcome_text_elt.text
			# проверяем правильность полученного текста
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
		finally:
			time.sleep(5)
			browser.quit()
			

