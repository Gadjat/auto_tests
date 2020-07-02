from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser=webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1")
    num2 = browser.find_element_by_css_selector("#num2")

    sum_num = int(num1.text)+int(num2.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum_num))

    button = browser.find_element_by_css_selector("button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

