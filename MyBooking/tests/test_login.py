import pytest
from pages.login_page import LoginPage
from utils.data_loader import get_test_data  # Import get_test_data function
#from pages.app_management_page import ApplicationManagementPage

# Load test data from Excel (use the path relative to this test file)
data = get_test_data("data/login_data.xlsx")  # Load the data into the 'data' variable
print("Excel rows loaded:", len(data))


# Parameterize the test with the loaded data
@pytest.mark.parametrize(
    "test_input",
    [data[0]],  # This will be the data loaded from the Excel file
    ids=lambda d: f"User={d['username']}"  # Custom IDs for each test
)
def test_login(page, test_input):
    
    # Initialize LoginPage and perform actions
    print("Starting Login Test")
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(test_input["username"], test_input["password"])
    page.wait_for_timeout(40000)
    page.get_by_role("button", name="Verify", exact=True).click()
    #page.wait_for_timeout(15000)
    #login_page.click_tab()
    page.wait_for_timeout(15000)
    print("LOGIN TEST FINISHED")

    