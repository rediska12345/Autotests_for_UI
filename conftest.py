import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from locators import Locators
from pages.order_page import OrderPage
import allure
from urls import Urls

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--window-size=1200,800")
        options.add_argument("--headless") 
        driver = webdriver.Firefox(options=options)
    
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def order_page_with_timeout(driver):
    order_page = OrderPage(driver)
    timeout =60 if driver.name == 'firefox' else 30
    return order_page, timeout


@pytest.fixture(scope='function')
@allure.step("Авторизация пользователя")
def user_login(driver, request):
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    login_page.get_login_page()
    login_page.user_login()
    login_page.wait_for_element_visibility(Locators.INGREDIENT)
    return driver