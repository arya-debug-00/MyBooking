from pages.overview_today_page import OverviewTodayPage
from utils.data_loader import get_test_data

register_data = get_test_data(
    "data/login_data.xlsx",
    sheet_name="RegisterOrder"
)


def test_fdx(logged_in_page):

    page = logged_in_page

    overview_page = OverviewTodayPage(page)

    overview_page.create_register(
        register_data[1]["CustomerNumber"]
    )

    overview_page.fill_register_order(
        register_data[1]
    )

    #overview_page.select_order_type("FDX")
    overview_page.select_order_type(register_data[1]["OrderType"])

    overview_page.create_order()