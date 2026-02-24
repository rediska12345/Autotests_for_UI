import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases_when_create_new_order(self, user_login):
        driver = user_login
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        order_page.get_order_page()
        total_orders_before = order_page.get_total_orders_count()
        
        main_page.get_main_page()
        main_page.drag_ingredient_to_constructor()
        main_page.create_order()
        
        order_page.get_order_page()
        total_orders_after = order_page.get_total_orders_count()
        
        assert total_orders_after > total_orders_before

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases_when_create_new_order(self, user_login):
        driver = user_login
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        order_page.get_order_page()
        today_orders_before = order_page.get_today_orders_count()
        
        main_page.get_main_page()
        main_page.drag_ingredient_to_constructor()
        main_page.create_order()
        
        order_page.get_order_page()
        today_orders_after = order_page.get_today_orders_count()
        
        assert today_orders_after > today_orders_before

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress_section(self, user_login):
        driver = user_login
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        order_page.get_order_page()
        orders_in_progress_before = order_page.get_orders_in_progress_count()
        
        main_page.get_main_page()
        main_page.drag_ingredient_to_constructor()
        main_page.create_order()
        order_number = main_page.get_order_number()
        
        order_page.get_order_page()
        orders_in_progress_after = order_page.get_orders_in_progress_count()
        last_order = order_page.get_last_order_in_progress()
        
        assert orders_in_progress_after > orders_in_progress_before
        assert order_number in last_order