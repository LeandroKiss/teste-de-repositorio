# o assert sempre verifica se o retorno da condição é True
assert True

assert numbers
num_esperado = 3
num_obtido = 2
assert num_esperado != num_obtido, f"esperado {num_esperado}. não é maior que o número atual {num_obtido} "

assert text
text_esperado = 'Selenium Webdriver'
text_obtido = 'Selenium webdriver'
assert text_esperado.lower() == text_obtido.lower(), f"esperado {text_esperado}. Atual {text_obtido}"

assert text in string
text_esperado = 'Selenium'
text_obtido = 'Selenium Webdriver'
assert text_esperado in text_obtido, f"esperando '{text_esperado}' dentro da strinng Atual '{text_obtido}'"

assert is_displayed/is_enabled/is_selected

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

# find_element()
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# send_keys
username.send_keys("standard_user")
time.sleep(5)
password.send_keys("secret_sauce")

# click
btn_login.click()

# text
products_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(products_title.text)
assert products_title.text == "Products"

# get_atribute
img_jacket = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[4]")
print (img_jacket.get_attribute("alt"))
assert img_jacket.get_attribute("alt") == "Sauce Labs Fleece Jacket"
assert img_jacket.is_displayed()
time.sleep(5)