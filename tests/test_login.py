import time
import pytest
from pythonProject1.pages.po_login import Login as Pol
import pandas as pd


@pytest.mark.smoke
def test_login_app(browser):
    time.sleep(5)

    lp = Pol(browser, "Admin", "admin123")
    browser.maximize_window()
    lp.enter_username()
    lp.enter_password()
    lp.click_login()
    time.sleep(10)


@pytest.mark.smoke
def test_kapil(browser):
    assert 4 == 5

    