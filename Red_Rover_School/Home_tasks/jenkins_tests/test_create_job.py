import time

from selenium.webdriver.common.by import By


def test_create_job(driver):
    driver.find_element(By.LINK_TEXT, 'Create a job').click()
    driver.find_element(By.ID, 'name').send_keys("")
    time.sleep(3)
    driver.find_element(By.ID, 'ok-button').click()
    res = driver.find_element(By.ID,'itemname-required')
    assert res.is_displayed()
