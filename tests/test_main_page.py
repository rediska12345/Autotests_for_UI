import allure
import pytest
from pages.main_page import MainPage
from locators import Locators
from urls import Urls


class TestMainPage:

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_click_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_on_element(Locators.ORDER_BUTTON)
        assert main_page.get_page_url() == Urls.ORDER_PAGE_URL

    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_on_element(Locators.ORDER_BUTTON)
        main_page.click_on_element(Locators.CONSTRUCTOR_BUTTON)
        assert main_page.get_page_url() == Urls.MAIN_PAGE_URL

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient_window_open_and_is_visible(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_on_element(Locators.INGREDIENT)
        assert main_page.is_element_present(Locators.INGREDIENT_WINDOW) == True

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_click_on_ingredient_window_close_and_is_not_visible(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_on_element(Locators.INGREDIENT)
        if main_page.is_element_present(Locators.INGREDIENT_WINDOW):
            main_page.click_on_element(Locators.INGREDIENT_WINDOW_CLOSE_BUTTON)
        assert main_page.is_element_not_present(Locators.INGREDIENT_WINDOW) == True

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        counter_value_before = main_page.get_counter_value(Locators.INGREDIENT_COUNTER)
        
        if driver.name == 'firefox':
            main_page.drag_ingredient_to_constructor_for_firefox(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
        else:
            main_page.drag_ingredient_to_constructor(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
            
        counter_value_after = main_page.get_counter_value(Locators.INGREDIENT_COUNTER)
        assert counter_value_after > counter_value_before