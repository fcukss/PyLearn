import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.INFO)
logging.getLogger('faker.factory').setLevel(logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.tabs
def test_new_tabs(driver, log_timing):
    driver.get("https://demoqa.com/browser-windows")
    logger.info(f"---> page is loaded at {log_timing()}s")
    logger.info(f"Current windowS: {driver.window_handles}")
    logger.info(f"current title: {driver.title}")

    tab_button = (WebDriverWait(driver, 7)
                  .until(EC.visibility_of_element_located((By.ID,"tabButton"))))
    logger.info(f"---> tab button is found at {log_timing}s")

    tab_button.click()
    logger.info(f"---> button is clicked at {log_timing}s")
    logger.info(f'current window: {driver.window_handles}')

    time.sleep(10)

@pytest.mark.alerts
def test_wait_new_alert(driver,log_timing):
    driver.get("https://demoqa.com/alerts")
    logger.info(f"---> page is loaded at {log_timing()}s")

    alert_button = (WebDriverWait(driver, 7)
                  .until(EC.visibility_of_element_located((By.ID, "alertButton"))))
    logger.info(f"---> alert button is found at {log_timing}s")

    alert_button.click()
    logger.info(f"---> alert_button is clicked at {log_timing}s")

    alert = driver.switch_to.alert
    logger.info(f"---> alert says {alert.text}")
    alert.accept()
    time.sleep(10)

@pytest.mark.frames
def test_frames(driver,log_timing):
    driver.get("https://demoqa.com/frames")
    logger.info(f"---> page is loaded at {log_timing()}s")

    frame1 = (WebDriverWait(driver, 7)
                    .until(EC.visibility_of_element_located((By.ID, "frame1"))))
    logger.info(f"---> frame is found at {log_timing}s. contains text{frame1.text}")

    driver.switch_to.frame(frame1)

    logger.info(driver.find_element(By.ID,"sampleHeading").text)

    time.sleep(10)
