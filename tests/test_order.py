import time
import allure
import pytest
from page_object.order_page import OrderPage
from CONSTANTS import URLS


order_data_set_1 = {"name":"Александр","fam_name":"Яковлев","adress":"Люблинская 15","metro":"Волжская","phone":"77777770112","rent_time":"сутки"}
order_data_set_2 = {"name":"Иван","fam_name":"Антонов","adress":"Островская 11","metro":"Выхино","phone":"77777770113","rent_time":"двое суток"}

@allure.epic('Проверка оформления заказа')
class Testorder:
    @allure.feature('Проверка оформления заказа через кнопку "заказать" в хэдере')
    @pytest.mark.parametrize('data',[order_data_set_1,order_data_set_2])
    def test_order_header_button(self, driver,data):
        order_page = OrderPage(driver)
        order_page.go_to_site(URLS.BASE_URL)
        order_page.close_cookie_overlay()
        order_page.click_order_button_header()
        order_page.fill_form_name(data["name"])
        order_page.fill_form_fam_name(data["fam_name"])
        order_page.fill_form_adress(data["adress"])
        order_page.fill_form_metro(data["metro"])
        order_page.fill_form_phone(data["phone"])
        order_page.press_next_page_but()
        order_page.fill_date()
        order_page.fill_rent_time(data["rent_time"])
        order_page.fill_color()
        order_page.press_order_but()
        order_page.press_confrim_but()
        order_page.check_pupup_text()
        order_page.close_order_confrimed_popup()
        order_page.click_scoot_logo_in_heder()
        order_page.check_if_main_page_url()
        order_page.click_yand_logo_in_header()
        order_page.check_redirect_zen()

    @allure.feature('Проверка оформления заказа через кнопку "заказать" внизу страницы')
    @pytest.mark.parametrize('data', [order_data_set_1, order_data_set_2])
    def test_order_down_button(self, driver, data):
        order_page = OrderPage(driver)
        order_page.go_to_site(URLS.BASE_URL)
        order_page.close_cookie_overlay()
        order_page.click_order_button_down()
        order_page.fill_form_name(data["name"])
        order_page.fill_form_fam_name(data["fam_name"])
        order_page.fill_form_adress(data["adress"])
        order_page.fill_form_metro(data["metro"])
        order_page.fill_form_phone(data["phone"])
        order_page.press_next_page_but()
        order_page.fill_date()
        order_page.fill_rent_time(data["rent_time"])
        order_page.fill_color()
        order_page.press_order_but()
        order_page.press_confrim_but()
        order_page.check_pupup_text()
        order_page.close_order_confrimed_popup()
        order_page.click_scoot_logo_in_heder()
        order_page.check_if_main_page_url()
        order_page.click_yand_logo_in_header()
        order_page.check_redirect_zen()


