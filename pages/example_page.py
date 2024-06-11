# pages/example_page.py
from selenium.webdriver.common.by import By


class ExamplePage:
    def __init__(self, driver):
        self.driver = driver
        self.example_element_locator = (By.ID, "example-element-id")

    def get_example_element(self):
        return self.driver.find_element(*self.example_element_locator)
