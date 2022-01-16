from cian_page import PerehodHelper


def test_perehod(driver):
    cian_main_page = PerehodHelper(driver)
    cian_main_page.go_to_site()
    assert 'Циан' in driver.title
    cian_main_page.serch_demand_button()
    assert 'https://spb.cian.ru/podbor-rieltora/' in driver.current_url





