from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import pytest
import logging
import time

@pytest.fixture()
def driver():
    service = EdgeService(executable_path=r"C:\webdrivers\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    # driver.implicitly_wait(3)  #time.spleep
    yield driver
    driver.quit()


# @pytest.fixture(autouse=True)
# def log_timing(request):
#     logger = logging.getLogger(request.node.name)
#     start = time.time()
#     logger.info(f"START: {request.node.name}")
#     yield
#     end = time.time()
#     logger.info(f"END: {request.node.name} - Duration: {end - start:.2f}s")

@pytest.fixture
def log_timing():
    start = time.time()

    def _elapsed():
        return round(time.time() - start, 2)

    return _elapsed