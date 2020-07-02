from selenium import webdriver
import os
import time
link = "http://suninjuly.github.io/file_input.html"
dir = os.path.abspath(os.path.dirname(__file__))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("Ivan@ivanov.ru")

    file_load = browser.find_element_by_css_selector("#file")
    file_load.send_keys(os.path.join(dir, 'test'))

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
