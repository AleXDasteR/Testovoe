import pytest
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage


def test_tensor_scenario(driver):
    sbis_page = SbisPage(driver)
    tensor_page = TensorPage(driver)

    # Сценарий
    sbis_page.open()
    sbis_page.go_to_contacts()
    sbis_page.click_tensor_banner()

    # Проверка на странице Тензора
    assert tensor_page.check_strength_in_people_block()
    tensor_page.go_to_more()
    tensor_page.verify_about_page()
    tensor_page.check_photo_sizes()
