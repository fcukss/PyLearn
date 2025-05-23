import logging
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.INFO)
logging.getLogger('faker.factory').setLevel(logging.INFO)
logger = logging.getLogger(__name__)

def test_red_box(driver):
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    driver.find_element(By.ID, 'adder').click()
    style = (WebDriverWait(driver, 5)
             .until(EC.visibility_of_element_located((By.ID, 'box0')))
             .get_attribute('style'))
    logger.info(style)


def test_button(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    button = driver.find_element(By.ID, 'enableAfter')
    print()
    print(f'{button.is_enabled()}')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(button))
    print(f'{button.is_enabled()}')

@pytest.mark.buttons
def test_wait_color_button(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    color_button = driver.find_element(By.ID, 'colorChange')
    WebDriverWait(driver, 7).until(
        EC.text_to_be_present_in_element_attribute((By.ID, 'colorChange'), 'class', 'danger'))
    assert color_button.value_of_css_property('color') == 'rgba(220, 53, 69, 1)'


def test_invisible_button(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    button = driver.find_element(By.ID, 'visibleAfter')
    print()

    print(f'{button.is_displayed()}')
    webelement = (WebDriverWait(driver, 5).until(EC.visibility_of(button)))
    print(f'{button.is_displayed()}')

    assert button is webelement
