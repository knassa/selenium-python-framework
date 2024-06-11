# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, *locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def find_elements(self, *locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))
