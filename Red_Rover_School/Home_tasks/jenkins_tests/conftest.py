from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import pytest

@pytest.fixture()
def driver():
    service = EdgeService(executable_path=r"C:\webdrivers\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get("https://jenkins-fly.fly.dev/")
    driver.find_element(By.ID, 'j_username').send_keys("admin")
    driver.find_element(By.ID, 'j_password').send_keys("admin")
    driver.find_element(By.NAME, 'Submit').click()
    yield driver
    driver.quit()