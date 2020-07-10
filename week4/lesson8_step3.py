import pytest
from selenium import webdriver
import time
import math
# pytest -v -m "smoke and not beta_users" test_fixture2.py




@pytest.mark.parametrize('link_list', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class Test():
    def test_param(self,browser,link_list):
        link = f"{link_list}"
        answer = math.log(int(time.time()))
        browser.get(link)

        input = browser.find_element_by_tag_name("textarea").send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission").click()

        text_hits = browser.find_element_by_class_name("smart-hints__hint").text
        assert text_hits == "Correct!", f"{text_hits}"


