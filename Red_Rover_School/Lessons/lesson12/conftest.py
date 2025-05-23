from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import pytest

@pytest.fixture()
def driver():
    service = EdgeService(executable_path=r"C:\webdrivers\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    # driver.implicitly_wait(3)  #time.spleep
    yield driver
    driver.quit()
