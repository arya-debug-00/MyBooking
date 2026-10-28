from pages.home_page import HomePage
from utils.data_loader import get_test_data


data = get_test_data("data/login_data.xlsx")
print(data[0])


def test_email_navigation(logged_in_page):

    page = logged_in_page

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
