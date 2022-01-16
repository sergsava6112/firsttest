from cian_page import PerehodHelper
import time


def test_perehod_to_demand_lending(driver):
    cian_main_page = PerehodHelper(driver)
    cian_main_page.go_to_site()
    assert 'Циан' in driver.title
    cian_main_page.serch_demand_button()
    assert 'https://spb.cian.ru/podbor-rieltora/' or 'https://www.cian.ru/podbor-rieltora/' in driver.current_url

def test_perehod_to_create_zayavka(driver):
    cian_main_page = PerehodHelper(driver)
    cian_main_page.go_to_site()
    assert 'Циан' in driver.title
    cian_main_page.serch_demand_button()
    cian_main_page.serch_perehod_bautton()
    assert 'https://www.cian.ru/application-form/' in driver.current_url
    time.sleep(5)




