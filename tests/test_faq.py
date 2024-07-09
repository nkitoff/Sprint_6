
import allure
import pytest

from page_object.faq_page import FaqPage
from CONSTANTS import URLS
@allure.epic('Проверка доступности раздела FAQ')
class TestFaq:
    @allure.feature('Тест FAQ')
    @pytest.mark.parametrize('number',[1,2,3,4,5,6,7,8])
    def test_faq(self, driver,number):
        faq_page = FaqPage(driver)
        faq_page.go_to_site(URLS.BASE_URL)
        faq_page.click_question(number)
        answer_text = faq_page.get_answer_text(number)
        expected_text = FaqPage.FAQ_TEXTS[number - 1]
        assert answer_text == expected_text, f"Ожидаемый текст '{expected_text}', фактический '{answer_text}'"


