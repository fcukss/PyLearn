from selenium import webdriver
from selenium.webdriver.common.by import By

def test_locked_out_user_error_message():
    driver = webdriver.Chrome()

    target_driver_version = "135.0.7049.85"
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
    driver.quit()

#135.0.7049.85

