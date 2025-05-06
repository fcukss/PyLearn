from selenium.webdriver.common.by import By


def test_logged(driver):
    res = driver.find_element(By.LINK_TEXT, 'Dashboard')
    assert res.is_displayed()

