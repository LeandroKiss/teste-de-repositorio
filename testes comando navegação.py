import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")
time.sleep(2)

driver.maximize_window()
time.sleep(1)

driver.refresh()
time.sleep(2)

driver.get("https://www.saucedemo.com/")
time.sleep(5)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(3)

driver.switch_to.new_window("tab")
time.sleep(3)

driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(3)

# driver.close()
# time.sleep(2)

driver.quit()

# get ()
# maximize_window()
# refresh ()
# back()
# forward()
# close()
# quit()
