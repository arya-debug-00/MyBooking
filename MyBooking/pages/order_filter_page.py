from playwright.sync_api import Page


class OrderFilterPage:

    def __init__(self, page: Page):

        self.page = page

        # Overview Today
        self.overview_today_icon = page.locator(
            'a[original-title="Overview Today"]'
        )

        # Order Number
        self.order_number_input = page.locator(
            'input[name="orderNumber"]'
        )

        # Pick-up Customer Name
        self.pickup_customer_name_input = page.locator(
            'input[name="locationCustomerName"]'
        )

        # Customer Number
        self.customer_number_input = page.locator(
            'input[name="customer"]'
        )

        # Customer Name
        self.customer_name_input = page.locator(
            'input[name="customerName"]'
        )

        # Address
        self.address_input = page.locator(
            'input[name="address"]'
        ).first

        # Date Fields
        self.date_inputs = page.locator(
            'input[placeholder="YYYY/MM/DD"]'
        )
        
        # Postal Code From
        self.postal_code_from_input = page.locator(
        'input[name="postalCodeFrom"]'
        )
        # Calendar Icons
        self.calendar_icons = page.locator(
            '[data-testid="CalendarIcon"]'
        )

        # All Inputs
        self.inputs = page.locator("input")

        # Checkboxes
        self.checkboxes = page.locator(
            'input.PrivateSwitchBase-input'
        )

        # Filter Button
        self.filter_button = page.get_by_role(
            "button",
            name="Filter"
        )

    def filter_order(self, data):

        self.overview_today_icon.click()

        print("Overview Today clicked")

        self.page.wait_for_timeout(5000)

        self.order_number_input.fill(
            str(data["OrderNumber"])
        )

        self.pickup_customer_name_input.fill(
            str(data["Pick-upCustomerName"])
        )

        self.customer_number_input.fill(
            str(data["CustomerNumber"])
        )

        self.customer_name_input.fill(
            str(data["CustomerName"])
        )

        self.address_input.fill(
            str(data["Address"])
        )
        self.postal_code_from_input.fill(
            str(data["PostelCodeFrom"])
        )
        print("Postal Code From filled")
        
        

        print("Postal Code From filled")
        # Contact Name
        self.inputs.nth(10).fill(
            str(data["ContactName"])
        )

        print("Contact Name filled")

        # Telephone
        self.inputs.nth(11).fill(
            str(data["TelephoneNumber"])
        )

        print("Telephone filled")

        # Email
        self.inputs.nth(12).fill(
            str(data["Email"])
        )

        print("Email filled")

        # #
        
        # Start Date

        start_day = str(data["StartDate"]).split(" ")[0].split("-")[-1].lstrip("0")

        print("Start Day:", start_day)

        self.calendar_icons.nth(0).click()

        print("Start Calendar opened")

        self.page.wait_for_timeout(2000)

        self.page.get_by_role(
            "gridcell",
            name=start_day,
            exact=True
        ).click()

        print("Start Date selected")

        # End Date

        end_day = str(data["EndDate"]).split(" ")[0].split("-")[-1].lstrip("0")

        print("End Day:", end_day)

        self.calendar_icons.nth(1).click()

        print("End Calendar opened")

        self.page.wait_for_timeout(2000)

        self.page.get_by_role(
            "gridcell",
            name=end_day,
            exact=True
        ).click()


        print("End Date selected")

        self.page.wait_for_timeout(2000)
        print("Order Number:", data["OrderNumber"])

        self.filter_button.click()

        print("Filter button clicked")

        self.page.wait_for_timeout(5000)