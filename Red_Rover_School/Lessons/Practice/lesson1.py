from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

# (pip install webdriver-manager)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

# code ...

driver.quit()