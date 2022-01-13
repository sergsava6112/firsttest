
from selenium.webdriver.common.keys import Keys
class TestCianPodbor:
    def test_perehod(self, driver):
        driver.get('https://www.cian.ru')
        assert 'Циан' in driver.title
        button = driver.find_element_by_xpath('//a[@href = "/podbor-rieltora/"]')
        button.send_keys(Keys.RETURN)
        assert 'https://spb.cian.ru/podbor-rieltora/' in driver.current_url


