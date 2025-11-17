import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",  # значение по умолчанию
        help="Choose language for browser: ru, en, es, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    
    # Получаем значение параметра --language
    language = request.config.getoption("--language")
    
    # Настраиваем опции браузера с учётом языка
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        'intl.accept_languages': language
    })
    
    # Инициализируем Chrome с заданными опциями
    browser = webdriver.Chrome(options=chrome_options)
    
    yield browser  # передаём браузер в тест
    
    print("\nquit browser..")
    browser.quit()



