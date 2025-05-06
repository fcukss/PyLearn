from credentials import URL, EDGE_DRIVER_PATH, USER_NAME, USER_PASSWORD
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_positive(driver):
    driver.get(URL)
    driver.find_element(By.ID, 'username').send_keys(USER_NAME)
    driver.find_element(By.ID, 'password').send_keys(USER_PASSWORD)
    driver.find_element(By.ID, 'submit').click()

    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"


def test_incorrect_user(driver):
    driver.get(URL)
    driver.find_element(By.ID, 'username').send_keys("IncorrectUsrer")
    driver.find_element(By.ID, 'password').send_keys("Password123")
    driver.find_element(By.ID, 'submit').click()

    error_message = driver.find_element(By.ID, "error")

    assert error_message.text == "Your username is invalid!"
