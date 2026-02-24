import allure
from pages.base_page import BasePage
from locators import Locators
from urls import Urls


class OrderPage(BasePage):

    @allure.step("Открыть страницу с лентой заказов")
    def get_order_page(self):
        self.get_page(Urls.ORDER_PAGE_URL)
        self.wait_for_element_visibility(Locators.ORDER_PAGE_HEADER)
    
    @allure.step("Получить количество выполненных заказов за все время")
    def get_total_orders_count(self):
        return int(self.get_text(Locators.TOTAL_ORDERS_VALUE))
    
    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text(Locators.TODAY_ORDERS_VALUE))
        
    @allure.step("Получить количество заказов в работе")
    def get_orders_in_progress_count(self):
        return len(self.find_elements_on_page(Locators.ORDERS_IN_PROCESS))
    
    @allure.step("Получить номер последнего заказа в работе")
    def get_last_order_in_progress(self):
        orders = self.find_elements_on_page(Locators.ORDERS_IN_PROCESS)
        return orders[-1].text if orders else None