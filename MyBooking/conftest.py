import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.data_loader import get_test_data


@pytest.fixture
def logged_in_page():
    data = get_test_data("data/login_data.xlsx")
    test_input = data[0]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)

        # Open login page
        login_page.navigate()

        # Username + Password + Login
        login_page.login(
            test_input["username"],
            test_input["password"]
        )

        # 40 seconds to manually get OTP from Outlook and type it
        page.wait_for_timeout(40000)

        # Click Verify
        page.get_by_role(
            "button",
            name="Verify",
            exact=True
        ).click()

        # Give application time to open
        page.wait_for_timeout(5000)

        # Give the logged-in page to the test
        yield page

        context.close()
        browser.close()
