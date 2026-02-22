import allure
from pages.base_page import BasePage
from locators import Locators
from urls import Urls


class OrderPage(BasePage):

    @allure.step("Открыть страницу с лентой заказов")
    def get_order_page(self):
        self.get_page(Urls.ORDER_PAGE_URL)
        self.wait_for_element_visibility(Locators.ORDER_PAGE_HEADER)
    
    @allure.step("Получить текущее количество выполненных заказов")
    def get_number_of_orders_created(self, duration):
        if duration == 'total':
            return self.get_text(Locators.TOTAL_ORDERS_VALUE)
        else:
            return self.get_text(Locators.TODAY_ORDERS_VALUE)
        
    @allure.step("Получить количество заказов в работе")
    def get_number_of_orders_in_progress(self):
        number_of_orders_in_progress = len(self.find_elements_on_page(Locators.ORDERS_IN_PROCESS))
        return number_of_orders_in_progress