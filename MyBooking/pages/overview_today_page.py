from playwright.sync_api import Page


class OverviewTodayPage:

    def __init__(self, page: Page):
        self.page = page

        # Overview Today icon
        self.overview_today_icon = page.locator('a[original-title="Overview Today"]')

        # Register link
        self.register_button = page.get_by_text(
            "Register",
            exact=True
        )

        # Customer Number search box
        self.customer_box = page.locator(
            'input[id="customers"]'
        )

        # Create button
        self.create_button = page.get_by_role(
            "button",
            name="Create"
        )

        # Address
        self.address_input = page.locator(
            'input[id="address"]'
        )

        # Postal Code
        self.postal_code_input = page.locator(
            'input[name="postalCode"]'
        )

        # Weight
        self.weight_input = page.locator(
            'input[name="weight"]'
        )

        # Parcels
        self.parcels_input = page.locator(
            'input[name="parcels"]'
        )

        # Pallets
        self.pallets_input = page.locator(
            'input[name="pallets"]'
        )

        # Create Order
        self.create_order_button = page.get_by_role("button",name="Create Order")


        # STK Checkbox
        self.stk_checkbox = page.get_by_text(
            "Styckegods",
            exact=True
        )

        # FDX Checkbox
        self.fdx_checkbox = page.get_by_text(
            "FDX",
            exact=True
        )
    def create_register(self, customer_number):

        self.overview_today_icon.click()

        print("Overview Today clicked")

        self.page.wait_for_timeout(3000)

        self.register_button.click()

        print("Register clicked")

        self.page.wait_for_timeout(3000)

        self.customer_box.click()

        self.customer_box.fill(str(customer_number))

        print("Customer Number:", customer_number)

        self.page.wait_for_timeout(3000)

        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(2000)

        self.create_button.click()

        print("Create clicked")

        self.page.wait_for_timeout(5000)

    def fill_register_order(self, data):

        self.address_input.fill(
            str(data["Address"])
        )

        self.postal_code_input.fill(
            str(data["PostalCode"])
        )

        self.weight_input.fill(
            str(data["Weight"])
        )

        self.parcels_input.fill(
            str(data["Parcels"])
        )

        self.pallets_input.fill(
            str(data["Pallets"])
        )

        print("Address:", data["Address"])
        print("PostalCode:", data["PostalCode"])
        print("Weight:", data["Weight"])
        print("Parcels:", data["Parcels"])
        print("Pallets:", data["Pallets"])  

    def select_order_type(self, order_type):

        checkboxes = self.page.locator(
            'input[type="checkbox"]'
        )

        if order_type.upper() == "STK":

            checkboxes.nth(0).check()

            print(
                "STK checked:",
                checkboxes.nth(0).is_checked()
            )

        elif order_type.upper() == "FDX":

            checkboxes.nth(1).check()

            print(
                "FDX checked:",
                checkboxes.nth(1).is_checked()
            )
    def create_order(self):

        self.create_order_button.click()

        print("Create Order clicked")

        self.page.wait_for_timeout(5000)

        print("Current URL:", self.page.url)

        print(self.page.locator("body").inner_text())