import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.data_loader import get_test_data


@pytest.fixture(scope="session")
def logged_in_page():

    print("===== LOGIN FIXTURE STARTED =====")

    #data = get_test_data("data/login_data.xlsx")
    data = get_test_data("data/login_data.xlsx",sheet_name="Login")
    print(data[0])
    test_input = data[0]

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )

        context = browser.new_context(
            no_viewport=True
        )

        page = context.new_page()

        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login(
            test_input["username"],
            test_input["password"]
        )

        page.wait_for_timeout(40000)

        page.get_by_role(
            "button",
            name="Verify",
            exact=True
        ).click()

        print("===== LOGIN SUCCESSFUL =====")

        page.wait_for_timeout(5000)

        yield page

        context.close()
        browser.close()