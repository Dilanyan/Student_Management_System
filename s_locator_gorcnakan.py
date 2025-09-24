from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest

driver = webdriver.Firefox()
try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    element1 = driver.find_element(By.ID, "user-name")
    element1.send_keys("standard_user")
    element2 = driver.find_element(By.ID,"password")
    element2.send_keys("secret_sauce")
    element3 = driver.find_element(By.NAME, "login-button")
    element3.click()
    element4 = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert element4.is_displayed()

except NoSuchElementException:
    print("Element not found!")
finally:
    driver.quit()