from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.base_page import BasePage
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class OrderLocators:
    INPUT_NAME = (By.XPATH,"//input[@placeholder='* Имя']")
    INPUT_FAM_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    INPUT_RENT_TIME = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    ITPUT_SCOOT_COLOR_BLACK = (By.XPATH,"//input[@id='black']")
    NEXT_PAGE_BUT = (By.XPATH,"//button[text()='Далее']")
    ORDER_BUT = (By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFRIM_BUT = (By.XPATH,"//button[contains(text(), 'Да')]")
    ORDER_CONFRIMED_TEXT_LOC = (By.XPATH,"//div[contains(text(), 'Заказ оформлен')]")
    SHOW_ORDER_BUT = (By.XPATH,"//button[contains(text(), 'Посмотреть статус')]")


class OrderPage(BasePage):
    # ожидаемый текст попапа с успешнм оформленим закзаа "Заказ оформлен"
    ORDERED_POPUP_TEXT = "Заказ оформлен"

    def fill_form_name(self,name):
        self.find_element_located(OrderLocators.INPUT_NAME).send_keys(name)

    def fill_form_fam_name(self,fam_name):
        self.find_element_located(OrderLocators.INPUT_FAM_NAME).send_keys(fam_name)

    def fill_form_adress(self,adress):
        self.find_element_located(OrderLocators.INPUT_ADRESS).send_keys(adress)

    def fill_form_metro(self, metro):
        self.find_element_located(OrderLocators.INPUT_METRO).click()
        locator = (By.XPATH, f"//div[@class='Order_Text__2broi'][contains(text(), '{metro}')]")
        self.find_element_located(locator).click()

    def fill_form_phone(self, phone):
        self.find_element_located(OrderLocators.INPUT_PHONE).send_keys(phone)

    def press_next_page_but(self):
        self.find_element_located(OrderLocators.NEXT_PAGE_BUT).click()


    def fill_date(self):
        current_date = datetime.now().strftime('%d.%m.%Y')
        date_input = self.find_element_located(OrderLocators.INPUT_DATE)
        date_input.send_keys(current_date)
        date_input.send_keys(Keys.ENTER)

    def fill_rent_time(self,rent_time):
        locator = (By.XPATH, f"//div[text()='{rent_time}']")

        self.find_element_located(OrderLocators.INPUT_RENT_TIME).click()
        self.find_element_located(locator).click()

    def fill_color(self):
        self.find_element_located(OrderLocators.ITPUT_SCOOT_COLOR_BLACK).click()

    def press_order_but(self):
        self.find_element_located(OrderLocators.ORDER_BUT).click()

    def press_confrim_but(self):
        self.find_element_located(OrderLocators.CONFRIM_BUT).click()

    def check_pupup_text(self):
        current_text = self.find_element_located(OrderLocators.ORDER_CONFRIMED_TEXT_LOC).text
        expected_text = self.ORDERED_POPUP_TEXT
        assert expected_text in current_text, f"Текст не совпадает. Текущий: {current_text}, ожидаемый {expected_text}"

    def close_order_confrimed_popup(self):
        self.find_element_located(OrderLocators.SHOW_ORDER_BUT).click()




