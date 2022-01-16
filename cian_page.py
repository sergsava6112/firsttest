from page import BasePage
from selenium.webdriver.common.by import By

class CianMainPageLocators:
    LOCATOR_CIAN_FILTERS_DEMAND = (By.XPATH, '//a[@href = "/podbor-rieltora/"]')
    LOCATOR_PODBOR = (By.XPATH, '//button[@data-name="SubmitButton"]')

class PerehodHelper(BasePage):

    def serch_demand_button(self):
        return self.find_element(CianMainPageLocators.LOCATOR_CIAN_FILTERS_DEMAND, time=2).click()

    def serch_perehod_bautton(self):
        return self.find_element(CianMainPageLocators.LOCATOR_PODBOR, time=2).click()




