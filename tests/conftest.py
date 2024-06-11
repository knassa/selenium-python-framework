# tests/conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.allure_helper import attach_screenshot
import datetime
from py.xml import html


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    if request.node.rep_call.failed:
        attach_screenshot(driver, name=request.node.nodeid)
    driver.quit()

def pytest_configure(config):
    config._metadata = {
        'Tester': 'Kapil Nassa',
        'Date': datetime.datetime.now().strftime("%Y-%m-%d")
    }


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Tester: Kapil Nassa")])
