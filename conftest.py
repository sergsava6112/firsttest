import pytest
from selenium import webdriver
from helper import CHROME_DRIVER_PATH

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    yield driver
    driver.quit()