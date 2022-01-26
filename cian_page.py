from page import BasePage
from selenium.webdriver.common.by import By

class CianMainPageLocators:

    LOCATOR_CIAN_FILTERS_DEMAND = (By.XPATH, '//a[@href = "/podbor-rieltora/"]')
    LOCATOR_CIAN_FILTERS_KUPIT = (By.XPATH, '//a[@href = "/kupit/"]')
    LOCATOR_CIAN_FILTERS_SNYAT = (By.XPATH, '//a[@href = "/snyat/"]')
    LOCATOR_CIAN_FILTERS_POSUTOCHNO = (By.XPATH, '//a[@href = "/posutochno/"]')
    LOCATOR_CIAN_FILTERS_KALK = (By.XPATH, '//a[@href = "/kalkulator-nedvizhimosti/"]')
    LOCATOR_CIAN_FILTERS_MORTGAGE = (By.XPATH, '//a[@href = "/mortgage/"]')
    LOCATOR_BUTTON_POISK = (By.XPATH, '//a[@data-mark="FiltersSearchButton"]')
    LOCATOR_BATTON_POISK_ON_MAP = (By.XPATH, '//a[@data-mark="FiltersSearchOnMapButton"]')
    LOCATOR_CIAN_LOGO = (By.XPATH, '//a[@data-name="Logo"]')

class DemandLendingLocators:
    LOCATOR_PODBOR = (By.XPATH, '//button[@data-name="SubmitButton"]')


class PerehodHelper(BasePage):

    def open_main_page(self):
        return self.base_url('https://www.cian.ru')

    def serch_demand_button(self):
        return self.find_element(CianMainPageLocators.LOCATOR_CIAN_FILTERS_DEMAND, time=2).click()

    def serch_perehod_button(self):
        return self.find_element(DemandLendingLocators.LOCATOR_PODBOR, time=2).click()




