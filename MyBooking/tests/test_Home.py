import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.data_loader import get_test_data


data = get_test_data("data/login_data.xlsx")
print(data[0])

@pytest.fixture(scope="function")
def page():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        #browser = p.chromium.launch(headless=False)
        context = browser.new_context(no_viewport=True)
        #context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_email_navigation(page):

    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(
        data[0]["username"],
        data[0]["password"]
    )

    page.wait_for_timeout(40000)

    page.get_by_role(
        "button",
        name="Verify",
        exact=True
    ).click()

    page.wait_for_timeout(5000)

    home_page = HomePage(page)

    home_page.click_home()

    page.wait_for_timeout(3000)

    home_page.click_email()

    page.wait_for_timeout(15000)

    home_page.create_email_list(
    data[0]["Title"],
    data[0]["Email"]
    )

    home_page.send_email(
    data[0]["Email"],
    data[0]["Content"]
    )
