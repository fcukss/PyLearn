from credentials import EDGE_DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By


def test_positive():
    options = EdgeOptions()
    service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=options)
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, 'username').send_keys("student")
        driver.find_element(By.ID, 'password').send_keys("Password123")
        driver.find_element(By.ID, 'submit').click()

        current_url = driver.current_url

        assert current_url == "https://practicetestautomation.com/logged-in-successfully/"
    finally:
        driver.quit()

def test_incorrect_user():
    options = EdgeOptions()
    service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=options)
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, 'username').send_keys("IncorrectUsrer")
        driver.find_element(By.ID, 'password').send_keys("Password123")
        driver.find_element(By.ID, 'submit').click()

        error_message = driver.find_element(By.ID, "error")

        assert error_message.text == "Your username is invalid!"
    finally:
        driver.quit()