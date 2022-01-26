from cian_page import PerehodHelper
from hamcrest import (
    assert_that,
    contains_string,
)


def test_open_demand_lending(driver):
    cian_main_page = PerehodHelper(driver)
    cian_main_page.go_to_site()
    cian_main_page.serch_demand_button()
    assert_that(driver.current_url, contains_string('cian.ru/podbor-rieltora/'), 'Не открылся лендинг заявок.')


def test_perehod_to_create_zayavka(driver):
    cian_main_page = PerehodHelper(driver)
    cian_main_page.go_to_site()
    cian_main_page.serch_demand_button()
    cian_main_page.serch_perehod_button()
    assert_that(driver.current_url, contains_string('/application-form/'), 'Не открылась форма создания заявки.')





