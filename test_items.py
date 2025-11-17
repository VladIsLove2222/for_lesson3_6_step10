import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_to_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    try:
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket[type='submit']"))
        )
        assert button.get_attribute('type') == 'submit'
        assert 'btn-add-to-basket' in button.get_attribute('class')
        
        print("Кнопка добавления в корзину найдена и активна")
        
    except Exception as e:
        pytest.fail(f"Ошибка при поиске кнопки добавления в корзину: {str(e)}")
