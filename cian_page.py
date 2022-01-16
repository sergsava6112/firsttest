from page import BasePage
from selenium.webdriver.common.by import By

class CianPageLocators:
    LOCATOR_CIAN_FILTERS_DEMAND = (By.XPATH, '//a[@href = "/podbor-rieltora/"]')

class PerehodHelper(BasePage):

    def serch_demand_button(self):
        return self.find_element(CianPageLocators.LOCATOR_CIAN_FILTERS_DEMAND, time=2).click()




