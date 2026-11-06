from pages.order_filter_page import OrderFilterPage
from utils.data_loader import get_test_data


order_filter_data = get_test_data(
    "data/login_data.xlsx",
    sheet_name="OrderFilter"
)


def test_order_filter(logged_in_page):

    page = logged_in_page

    order_filter_page = OrderFilterPage(page)

    order_filter_page.filter_order(
        order_filter_data[0]
    )