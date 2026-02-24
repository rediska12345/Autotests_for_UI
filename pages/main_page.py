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
    def click_order_button(self):
        self.click_on_element(Locators.ORDER_BUTTON)
        self.wait_for_element_visibility(Locators.ORDER_PAGE_HEADER)
    
    @allure.step("Кликнуть по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_on_element(Locators.CONSTRUCTOR_BUTTON)
        self.wait_for_element_visibility(Locators.INGREDIENT)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_on_element(Locators.INGREDIENT)
    
    @allure.step("Проверить отображение окна ингредиента")
    def is_ingredient_window_visible(self):
        return self.is_element_visible(Locators.INGREDIENT_WINDOW)
    
    @allure.step("Закрыть окно ингредиента")
    def close_ingredient_window(self):
        self.click_on_element(Locators.INGREDIENT_WINDOW_CLOSE_BUTTON)
        self.wait_for_element_invisibility(Locators.INGREDIENT_WINDOW)
    
    @allure.step("Проверить, что окно ингредиента закрыто")
    def is_ingredient_window_closed(self):
        return self.is_element_not_visible(Locators.INGREDIENT_WINDOW)
    
    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        return self.get_counter_value(Locators.INGREDIENT_COUNTER)
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        self.drag_ingredient_to_constructor(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
    
    @allure.step("Создать заказ")
    def create_order(self):
        self.click_on_element(Locators.CREATE_ORDER_BUTTON)
        self.wait_for_element_visibility(Locators.ORDER_CONFIRMATION_WINDOW)
    
    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text(Locators.ORDER_NUMBER)