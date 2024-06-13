import time
import pytest
from pages.po_login import Login as Pol

@pytest.mark.login
def test_login_app(browser):
    time.sleep(5)
    lp = Pol(browser, "Admin", "admin123")
    browser.maximize_window()
    lp.enter_username()
    lp.enter_password()
    lp.click_login()
    time.sleep(10)

