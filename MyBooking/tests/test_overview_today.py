from pages.overview_today_page import OverviewTodayPage
from utils.data_loader import get_test_data

customer_data = get_test_data(
    "data/login_data.xlsx",
    sheet_name="CustomerNumber"
)


def test_overview_today(logged_in_page):

    page = logged_in_page

    overview_today_page = OverviewTodayPage(page)
    print(page.url)

    overview_today_page.create_register(
        customer_data[0]["CustomerNumber"]
    )