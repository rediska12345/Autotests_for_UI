import allure
from pages.base_page import BasePage
from locators import Locators
from data import Credentials
from urls import Urls

class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def get_login_page(self):
        self.get_page(Urls.LOGIN_PAGE_URL)
        self.wait_for_element_visibility(Locators.LOGIN_EMAIL)

    @allure.step("Войти в аккаунт")
    def user_login(self):
        self.enter_data(Locators.LOGIN_EMAIL, Credentials.EMAIL)
        self.enter_data(Locators.LOGIN_PASSWORD, Credentials.PASSWORD)
        import time
        time.sleep(1)
        if self.driver.name == 'firefox':
            self.click_with_js(Locators.LOGIN_BUTTON)
        else:
            self.click_on_element(Locators.LOGIN_BUTTON)
            
        self.wait_for_element_visibility(Locators.INGREDIENT)