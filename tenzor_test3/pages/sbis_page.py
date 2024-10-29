from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class SBISPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://sbis.ru/')

    def go_to_downloads(self):
        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Скачать локальные версии"))
        )
        contacts_link.click()

    def download_plugin(self):
        download_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Скачать (Exe 11.48 МБ)'))
        )
        download_button.click()
        time.sleep(10)

    def compare_sizes(self):
        plugin_name = 'sbisplugin-setup-web.exe'
        file_size = str(os.stat(plugin_name).st_size)
        return '11.48' in file_size
