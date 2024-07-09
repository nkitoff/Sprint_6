from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CONSTANTS import URLS


class BasePageLocators:
    ORDER_BUT_HEAD = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUT_DOWN = (By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    COOKIE_POPOUP_BUT = (By.XPATH,"//button[@id='rcc-confirm-button']")
    SCOOT_LOGO_HEAD_BUT = (By.XPATH, "//div[@class='Header_Logo__23yGT']")
    YAND_LOGO_HEAD_BUT = (By.XPATH,"//a[@class='Header_LogoYandex__3TSOI']")

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not found {locator}')

    def click_order_button_header(self):
        self.find_element_located(BasePageLocators.ORDER_BUT_HEAD).click()

    def click_order_button_down(self):
        self.find_element_located(BasePageLocators.ORDER_BUT_DOWN).click()

    def close_cookie_overlay(self):
        self.find_element_located(BasePageLocators.COOKIE_POPOUP_BUT).click()

    def click_scoot_logo_in_heder(self):
        self.find_element_located(BasePageLocators.SCOOT_LOGO_HEAD_BUT).click()

    def click_yand_logo_in_header(self):
        self.find_element_located(BasePageLocators.YAND_LOGO_HEAD_BUT).click()

    def check_redirect_zen(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        WebDriverWait(self.driver, 10).until(EC.url_contains(URLS.ZEN_URL))
        expected_url = URLS.ZEN_URL
        current_url = self.driver.current_url
        assert expected_url in current_url, f"Ожидаемый URL: {expected_url}, фактический: {current_url}"

    def check_if_main_page_url(self):
        current_url = self.driver.current_url
        assert current_url == URLS.BASE_URL




