from selenium import webdriver
import time
import math
link = "https://stepik.org/lesson/236895/step/1"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    answer = math.log(int(time.time()))
    input = browser.find_element_by_class_name("textarea")
    input.send_keys(str(answer))
    button = browser.find_element_by_class_name("submit-submission").click()

    text_hits = browser.find_element_by_class_name("smart-hints__hint").text()
    print(text_hits)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

