from selenium.webdriver.common.by import By

class SbisPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://sbis.ru/")

    def go_to_contacts(self):
        contacts_link = self.driver.find_element(By.LINK_TEXT, "Контакты")
        contacts_link.click()

    def click_tensor_banner(self):
        tensor_banner = self.driver.find_element(By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
        tensor_banner.click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
