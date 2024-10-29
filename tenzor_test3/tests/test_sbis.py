from pages.sbis_page import SBISPage

def test_initial_region_and_partners(driver):
    sbis_page = SBISPage(driver)
    sbis_page.go_to_downloads()
    sbis_page.download_plugin()
    sbis_page.compare_sizes()
