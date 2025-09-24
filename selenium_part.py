from selenium import webdriver
from selenium_helper import Selenium_helper

drivers = [webdriver.Firefox(), webdriver.Chrome(), webdriver.Edge()]
for driver in drivers:
    Selenium_helper.do_some_rutin(driver)
