import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу сайта")
    def get_page(self, url):
        self.driver.get(url)

    @allure.step("Подождать видимости элемента")
    def wait_for_element_visibility(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout, poll_frequency=2).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Подождать невидимости элемента")
    def wait_for_element_invisibility(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout, poll_frequency=2).until(EC.invisibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element_visibility(locator, timeout)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        self.wait_for_element_visibility(locator)
        element = self.find_element_on_page(locator)
        return element.text
    
    @allure.step("Поиск элемента на странице")
    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Найти элементы на странице")
    def find_elements_on_page(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Получить URL страницы")
    def get_page_url(self):
        return self.driver.current_url
    
    @allure.step("Проверить, что элемент отображается")
    def is_element_present(self, locator):
        if self.wait_for_element_visibility(locator):
            return True
        else:
            return False
        
    @allure.step("Проверить, что элемент не отображается")
    def is_element_not_present(self, locator):
        if self.wait_for_element_invisibility(locator):
            return True
        else:
            return False
        
    @allure.step("Получить значение счетчика")
    def get_counter_value(self, locator, timeout=10):
        element = self.wait_for_element_visibility(locator, timeout)
        return int(element.text)
        
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self, ingredient_locator, constructor_locator, timeout=10):
        ingredient = self.wait_for_element_visibility(ingredient_locator, timeout)
        constructor = self.wait_for_element_visibility(constructor_locator, timeout)
        action = ActionChains(self.driver)
        action.click_and_hold(ingredient).move_to_element(constructor).release().perform()

    @allure.step("Перетащить ингредиент в конструктор в Firefox")
    def drag_ingredient_to_constructor_for_firefox(self, ingredient_locator, constructor_locator, timeout=10):
        """
        Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
        :param source_locator: Локатор элемента, который нужно перетащить.
        :param target_locator: Локатор элемента, куда нужно перетащить.
        """
        ingredient = self.wait_for_element_visibility(ingredient_locator, timeout)
        constructor = self.wait_for_element_visibility(constructor_locator, timeout)
        
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, ingredient, constructor)
   
    @allure.step("Вводим данные в поле")
    def enter_data(self, locator, data, timeout = 10):
        data_input = self.wait_for_element_visibility(locator, timeout)
        data_input.clear()
        data_input.send_keys(data)
        
    @allure.step("Кликнуть на элемент с помощью JavaScript")
    def click_with_js(self, locator, timeout=10):
        element = self.wait_for_element_visibility(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)