import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="session")
def driver():
    project_path = os.path.abspath(".")
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": project_path,  # Указываем путь для загрузки
        "download.prompt_for_download": False,  # Отключаем запрос на сохранение
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()