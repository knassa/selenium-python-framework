# tests/conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import datetime
from py.xml import html
from utils.test_data import TestConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(TestConfig.BASE_URL)
    yield driver
    driver.get(TestConfig.BASE_URL)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test has failed
    if report.when == "call" and report.failed:
        # Access the browser fixture
        driver = item.funcargs.get('browser')
        if driver:
            # Take a screenshot and save it
            screenshot_path = f"screenshots/{item.nodeid.replace('::', '_')}.png"
            driver.save_screenshot(screenshot_path)

@pytest.fixture(scope="session", autouse=True)
def configure_directories():
    import os
    os.makedirs("screenshots", exist_ok=True)


def pytest_configure(config):
    config._metadata = {
        'Tester': 'Kapil Nassa',
        'Date': datetime.datetime.now().strftime("%Y-%m-%d")
    }


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Tester: Kapil Nassa")])
