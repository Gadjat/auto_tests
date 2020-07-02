from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),("$100")))

    button1 = browser.find_element_by_css_selector("#book").click()

    num = browser.find_element_by_css_selector("#input_value").text
    x = calc(num)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(str(x))

    button2 = browser.find_element_by_css_selector("#solve").click()

finally:
    time.sleep(30)
    browser.quit()
