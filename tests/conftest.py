from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from py.xml import html
from pythonProject1.utils.test_data import TestConfig


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

# check for commit 4th
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call,config):
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
    config._metadata = {
        'Tester': 'Kapil Nassa',
        'Date': datetime.now().strftime("%Y-%m-%d")
    }

    today = datetime.now()
    report_dir = Path("pytest_reports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Pytest_Report_{'%Y%m%d%H%M'}.html"
    config.option.htmlpath = report_dir
    config.option.self_contained_html = True


@pytest.fixture(scope="session", autouse=True)
def configure_directories():
    import os
    os.makedirs("screenshots", exist_ok=True)


def pytest_html_report_title(report):
    report.title = "PyTest Report"


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Tester: Kapil Nassa")])
