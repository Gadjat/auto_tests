from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button").click()

    confrim = browser.switch_to_alert().accept()

    num = browser.find_element_by_css_selector("#input_value").text
    x = calc(num)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(str(x))

    button2 = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(30)
    browser.quit()
