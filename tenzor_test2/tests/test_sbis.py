from pages.sbis_page import SBISPage

def test_initial_region_and_partners(driver):
    sbis_page = SBISPage(driver)
    sbis_page.go_to_contacts()

    assert "Республика Татарстан" in sbis_page.get_region(), "Регион не соответствует!"
    assert sbis_page.is_partners_list_displayed(), "Список партнеров не отображается!"
    sbis_page.change_region()

    assert "Камчатский край" in sbis_page.get_region(), "Регион не изменился!"
    assert sbis_page.is_partners_list_displayed(), "Список партнеров не обновился!"
    assert "kamchatskij-kraj" in sbis_page.get_current_url().lower(), "URL не содержит выбранный регион!"
    assert "Камчатский край" in sbis_page.get_page_title(), "Title не содержит выбранный регион!"
