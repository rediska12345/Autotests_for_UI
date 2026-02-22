import allure
from pages.base_page import BasePage
from urls import Urls
from locators import Locators

class MainPage(BasePage):     

    @allure.step("Открытие главной страницы")
    def get_main_page(self):
        self.get_page(Urls.MAIN_PAGE_URL)
        self.wait_for_element_visibility(Locators.INGREDIENT)

    @allure.step("Кликнуть по кнопке 'Лента заказов'")
    def click_order_button(self, locator):
        self.click_on_element(locator)   
    
    @allure.step("Кликнуть по кнопке 'Конструктор'")
    def click_constructor_button(self, locator):
        self.click_on_element(locator) 
   
    @allure.step("Закрыть окно ингредиента кликнув по крестику")
    def close_ingredient_window(self, locator):
        self.click_on_element(locator)
    
    