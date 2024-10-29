from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SBISPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://sbis.ru/')

    def go_to_contacts(self):
        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Контакты"))
        )
        contacts_link.click()

    def get_region(self):
        region_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'))
        )
        time.sleep(2)
        return region_element.text

    def is_partners_list_displayed(self):
        return bool(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div'))
        ))

    def change_region(self):
        region_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'))
        )
        region_dropdown.click()

        new_region_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span'))
        )
        new_region_option.click()

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title