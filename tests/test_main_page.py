import allure
import pytest
from pages.main_page import MainPage
from urls import Urls


class TestMainPage:

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_click_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_order_button()
        
        assert main_page.get_page_url() == Urls.ORDER_PAGE_URL

    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_order_button()
        main_page.click_constructor_button()
        
        assert main_page.get_page_url() == Urls.MAIN_PAGE_URL

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient_window_open_and_is_visible(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_ingredient()
        
        assert main_page.is_ingredient_window_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_click_on_ingredient_window_close_and_is_not_visible(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_ingredient()
        main_page.close_ingredient_window()
        
        assert main_page.is_ingredient_window_closed()

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        
        counter_value_before = main_page.get_ingredient_counter_value()
        main_page.drag_ingredient_to_constructor()
        counter_value_after = main_page.get_ingredient_counter_value()
        
        assert counter_value_after > counter_value_before