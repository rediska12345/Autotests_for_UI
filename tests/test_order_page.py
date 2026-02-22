import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators import Locators
from urls import Urls


class TestOrderPage:

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases_when_create_new_order(self, user_login):
        driver = user_login
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_on_element(Locators.ORDER_BUTTON)
        total_orders_before = order_page.get_number_of_orders_created('total')
        
        main_page.get_main_page()
        
        if driver.name == 'firefox':
            main_page.drag_ingredient_to_constructor_for_firefox(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
        else:
            main_page.drag_ingredient_to_constructor(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
            
        main_page.click_on_element(Locators.CREATE_ORDER_BUTTON)
        
        order_page.get_order_page()
        total_orders_after = order_page.get_number_of_orders_created('total')
        
        assert total_orders_after > total_orders_before

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases_when_create_new_order(self, user_login):
        driver = user_login
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_on_element(Locators.ORDER_BUTTON)
        today_orders_before = order_page.get_number_of_orders_created('today')
        
        main_page.get_main_page()
        
        if driver.name == 'firefox':
            main_page.drag_ingredient_to_constructor_for_firefox(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
        else:
            main_page.drag_ingredient_to_constructor(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
            
        main_page.click_on_element(Locators.CREATE_ORDER_BUTTON)
        
        order_page.get_order_page()
        today_orders_after = order_page.get_number_of_orders_created('today')
        
        assert today_orders_after > today_orders_before

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress_section(self, user_login):
        driver = user_login
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_on_element(Locators.ORDER_BUTTON)
        orders_in_progress_before = order_page.get_number_of_orders_in_progress()
        
        main_page.get_main_page()
        
        if driver.name == 'firefox':
            main_page.drag_ingredient_to_constructor_for_firefox(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
        else:
            main_page.drag_ingredient_to_constructor(Locators.INGREDIENT, Locators.CONSTRUCTOR_DROP_AREA)
            
        main_page.click_on_element(Locators.CREATE_ORDER_BUTTON)
        
        order_page.get_order_page()
        orders_in_progress_after = order_page.get_number_of_orders_in_progress()
        
        assert orders_in_progress_after > orders_in_progress_before