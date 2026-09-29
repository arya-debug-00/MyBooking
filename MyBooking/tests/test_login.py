import pytest
from pages.login_page import LoginPage
from utils.data_loader import get_test_data  # Import get_test_data function

# Load test data from Excel (use the path relative to this test file)
data = get_test_data("data/login_data.xlsx")  # Load the data into the 'data' variable


@pytest.fixture(scope="function")
def page():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

# Parameterize the test with the loaded data
@pytest.mark.parametrize(
    "test_input",
    data,  # This will be the data loaded from the Excel file
    ids=lambda d: f"User={d['username']}"  # Custom IDs for each test
)
def test_login(page, test_input):
    
    # Initialize LoginPage and perform actions
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(test_input["username"], test_input["password"])
    