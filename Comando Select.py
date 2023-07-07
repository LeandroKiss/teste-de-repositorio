import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')

dropdown_products = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
dropdown_products.select_by_visible_text("Yahoo")
time.sleep(2)

dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_visible_text("Avatar")
time.sleep(2)
dropdown_animals.select_by_index(2)
time.sleep(2)

dropdown_food = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
dropdown_food.select_by_visible_text("Bonda")
time.sleep(2)
dropdown_food.select_by_visible_text("Pizza")
dropdown_food.select_by_visible_text("Burger")
