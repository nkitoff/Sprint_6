from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class FaqPageLocators:
    ALL_QUESTIONS = (By.XPATH,"(//div[@class='accordion__heading'])")
    ALL_ANSWERS = (By.XPATH,"//div[@class='accordion__panel']")





class FaqPage(BasePage):
    FAQ_TEXTS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]

    def click_question(self, number):
        questions = self.find_elements_located(FaqPageLocators.ALL_QUESTIONS)
        question = questions[number - 1]
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        ActionChains(self.driver).move_to_element(question).click(question).perform()

    def get_answer_text(self, number):
        answer_locator = (By.XPATH, f"(//div[@class='accordion__panel'])[{number}]")
        answer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return answer.text

