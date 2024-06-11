# utils/browser.py
from selenium import webdriver


def get_driver(browser_name):
    if browser_name.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        return webdriver.Chrome(options=options)
    elif browser_name.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        return webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
