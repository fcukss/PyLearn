from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from credentials import EDGE_DRIVER_PATH

def test_locked_out_user_error_message():
    options = EdgeOptions()
    service = EdgeService(executable_path=EDGE_DRIVER_PATH)

    driver = webdriver.Edge(service=service, options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, 'user-name').send_keys("locked_out_user")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()

        wait = WebDriverWait(driver, 10)
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))

        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
    finally:
        driver.quit()