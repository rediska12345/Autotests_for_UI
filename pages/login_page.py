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
        self.click_on_element(Locators.LOGIN_BUTTON)
        # Ждем успешной авторизации
        self.wait_for_element_visibility(Locators.CREATE_ORDER_BUTTON)