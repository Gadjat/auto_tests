from selenium import webdriver
from selenium.webdriver.support.ui import Select
from string import ascii_letters
import time
import random
from random import choice

mail_list=[]
mail_list.append("test" + str(random.randint(0,99999)) + "@stepik.ru")

browser = webdriver.Chrome()


# кейс 1, регистрация
try:
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    browser.get(link)

    input_email = browser.find_element_by_css_selector("#id_registration-email").send_keys(mail_list[0])

    input_password = browser.find_element_by_css_selector("#id_registration-password1").send_keys(mail_list[0])

    input_password_confirme = browser.find_element_by_css_selector("#id_registration-password2").send_keys(mail_list[0])

    button = browser.find_element_by_name("registration_submit").click()

    welcome_text = browser.find_element_by_class_name("alertinner.wicon").text

    assert "Спасибо за регистрацию!" == welcome_text

finally:
    exit = browser.find_element_by_css_selector("#logout_link").click()


# кейс 2, авторизация
def auth():
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    browser.get(link)

    input_login = browser.find_element_by_css_selector("#id_login-username").send_keys(mail_list[0])

    input_login_password = browser.find_element_by_css_selector("#id_login-password").send_keys(mail_list[0])

    button = browser.find_element_by_name("login_submit").click()

    welcome_text = browser.find_element_by_class_name("alertinner.wicon").text

    assert "Рады видеть вас снова" == welcome_text
    return
try:
    auth()
finally:
    exit = browser.find_element_by_css_selector("#logout_link").click()


# кейс 3, Смена локали

try:
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)

    location_select = Select(browser.find_element_by_css_selector("select.form-control"))
    location_select.select_by_value("ro")

    button = browser.find_element_by_css_selector("#language_selector > button").click()

    store_menu = browser.find_element_by_css_selector("a.dropdown-toggle").text
    basket = browser.find_element_by_css_selector("strong").text
    login = browser.find_element_by_css_selector("#login_link").text

    assert "Exploreaza magazin" == store_menu
    assert "Total in cos:" == basket
    assert "Intra in cont sau inregistreaza-te" == login

finally:
    location_select_reverse = Select(browser.find_element_by_css_selector("select.form-control"))
    location_select_reverse.select_by_value("ru")
    button_reverse = browser.find_element_by_css_selector("#language_selector > button").click()

# кейс 4, Редактирование профиля

try:
    auth()

    account = browser.find_element_by_xpath('//a[@href="/ru/accounts/"]/i').click()

    account_ed = browser.find_element_by_xpath('//a[@href="/ru/accounts/profile/edit/"]').click()

    name_input = browser.find_element_by_id("id_first_name").send_keys(''.join(choice(ascii_letters) for i in range(10)))

    last_name_input = browser.find_element_by_id("id_last_name").send_keys(''.join(choice(ascii_letters) for i in range(10)))

    button = browser.find_element_by_class_name("btn.btn-lg.btn-primary").click()

    save_ed = browser.find_element_by_class_name("alertinner.wicon").text

    assert "Профиль обновлен" == save_ed

finally:
    exit = browser.find_element_by_id("logout_link").click()


# кейс 5,Добавление и удаление товаров. Корзина

try:
    auth()
    # добавление
    products = browser.find_element_by_xpath('//a[@href="/ru/catalogue/"]').click()

    choice = browser.find_element_by_css_selector(".col-xs-6.col-sm-4.col-md-3.col-lg-3 i.icon-ok")

    basket_choice = browser.find_element_by_class_name("btn.btn-primary.btn-block").click()

    name_choice = browser.find_element_by_css_selector(".col-xs-6.col-sm-4.col-md-3.col-lg-3 h3 a").text

    basket_info = browser.find_element_by_xpath('//a[@href="/ru/basket/"][@class="btn btn-info"]').click()

    check = browser.find_element_by_css_selector("div.col-sm-4 h3 a").text

    assert name_choice == check
    # удаление
    delete = browser.find_element_by_css_selector('[data-behaviours="remove"]').click()
    basket_is_empty = browser.find_element_by_css_selector("div.alertinner p").text # на этом моменте падает(кнопка из предыдущего шага на сайте не работает)

    assert "Ваша корзина теперь пуста" == basket_is_empty

finally:
    exit = browser.find_element_by_id("logout_link").click()
    browser.quit()




