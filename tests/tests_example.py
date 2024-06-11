# tests/test_example.py
import pytest
from pages.example_page import ExamplePage


@pytest.mark.smoke
def test_example(browser):
    # Initialize the page object
    example_page = ExamplePage(browser)

    # Navigate to the example page
    browser.get("http://google.com")

    # Verify that the example element is displayed
    assert example_page.get_example_element().is_displayed()
