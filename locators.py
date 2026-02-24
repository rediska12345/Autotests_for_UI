from selenium.webdriver.common.by import By

class Locators:
    # Локаторы страницы логина
    LOGIN_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    LOGIN_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    
    # Локаторы главной страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Конструктор']]")
    ORDER_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Лента Заказов']]")
    INGREDIENT = (By.XPATH, "(//a[contains(@href, '/ingredient/')])[1]")
    INGREDIENT_COUNTER = (By.XPATH, "(//a[contains(@href, '/ingredient/')]//p[contains(@class, 'counter')])[1]")
    INGREDIENT_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    INGREDIENT_WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//h2")
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//h2")
    
    # Локаторы страницы заказов
    ORDER_PAGE_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')
    TOTAL_ORDERS_VALUE = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_ORDERS_VALUE = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    ORDERS_IN_PROCESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li')
    
    # Локаторы страницы регистрации
    REGISTRATION_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    REGISTRATION_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    REGISTRATION_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    REGISTRATION_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    REGISTRATION_VERIFY = (By.XPATH, '//button[text()="Войти"]')