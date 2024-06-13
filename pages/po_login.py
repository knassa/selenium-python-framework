
from selenium.webdriver.common.by import By


class Login:
    username_loc = (By.XPATH, "//input[@name = 'username']")
    password_loc = (By.XPATH, "//input[@name = 'password']")
    login_button_loc = (By.XPATH, "//*[@type= 'submit']")

    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def enter_username(self):
        self.driver.find_element(*self.username_loc).send_keys(self.username)

    def enter_password(self):
        self.driver.find_element(*self.password_loc).send_keys(self.password)

    def click_login(self):
        self.driver.find_element(*self.login_button_loc).click()
