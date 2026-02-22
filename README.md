Диплом 3 часть
Студент: Бритвина Надежда
Когорта: #36
# Автотесты UI 

Проект содержит Автотесты для UI веб-приложения Stellar Burgers.

## Структура проекта
- `pages/`
- `tests/`
- `url.py`
- `conftest.py`
- `data.py`
- `requirements.txt`
- `locators.py` 

### Запуск всех тестов
pytest

#### Запуск с генерацией Allure отчета
pytest tests/ -v -s --alluredir=allure-results

##### Просмотр Allure отчета
allure serve allure_results