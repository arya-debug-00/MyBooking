import pytest
from pages.app_management_page import ApplicationManagementPage
from utils.data_loader import get_test_data

# Load Excel data
data = get_test_data("data/login_data.xlsx")

create_input = data[0]
edit_input = data[1]



def open_edi_filter(page):

    app_management_page = ApplicationManagementPage(page)

    app_management_page.click_application_management()

    app_management_page.click_edi_filter()

    page.wait_for_timeout(5000)

    return app_management_page

def test_create_edi_filter(logged_in_page):

    page = logged_in_page

    app_management_page = open_edi_filter(page)

    app_management_page.create_edi_filter(create_input)

    page.wait_for_timeout(10000)


def test_edit_edi_filter(logged_in_page):

    page = logged_in_page

    app_management_page = open_edi_filter(page)

    print(
        "Records before edit:",
        page.locator(
            "div.filterList",
            has_text=create_input["note"]
        ).count()
    )

    app_management_page.click_edit_by_note(
        create_input["note"]
    )

    page.wait_for_timeout(3000)

    print(
        "Note after Edit opens:",
        app_management_page.note_input.input_value()
    )

    app_management_page.edit_edi_filter(edit_input)

    page.wait_for_timeout(5000)

    print(
        "Old note records:",
        page.locator(
            "div.filterList",
            has_text=create_input["note"]
        ).count()
    )

    print(
        "New note records:",
        page.locator(
            "div.filterList",
            has_text=edit_input["note"]
        ).count()
    )

    page.wait_for_timeout(10000)