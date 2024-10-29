from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TensorPage:
    def __init__(self, driver):
        self.driver = driver

    def check_strength_in_people_block(self):
        try:
            strength_block = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'))
            )
            return strength_block.is_enabled()
        except Exception as e:
            print(f"Ошибка при поиске блока сила в людях: {e}")
            return False

    def go_to_more(self):
        time.sleep(5)
        xpath = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
        link = self.driver.find_element(By.XPATH, xpath)
        link.click()

        # Ждём, пока страница загрузится
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://tensor.ru/about")  # Проверяем, что URL изменился на нужный
        )

    def verify_about_page(self):
        assert self.driver.current_url == "https://tensor.ru/about"

    def check_photo_sizes(self):
        photos = self.driver.find_elements(By.XPATH, "//img")[1:5]
        sizes = [(photo.size['width'], photo.size['height']) for photo in photos]
        assert all(size == sizes[0] for size in sizes)
