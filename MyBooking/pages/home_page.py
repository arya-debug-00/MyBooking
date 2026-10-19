from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # Home icon
        self.home_button = page.locator('a[original-title="Home"]')

        # Email option under Contact
        self.email_button = page.get_by_text("Email", exact=True)

        # Email page
        self.create_email_list_button = page.get_by_role(
            "button",
            name="Create e-mail list"
        )

        self.title_input = page.locator('input[name="title"]')

        self.emails_input = page.locator('input[name="emails"]').nth(1)

        self.create_button = page.get_by_role("button",name="create")


        # Send Email

        self.email_list_dropdown = page.locator(
            'input[name="emails"][role="combobox"]'
        )

        self.content_box = page.locator(
            'textarea[name="content"]'
        )

        self.custom_checkbox = page.get_by_text("Customs")

        self.bookingimport_checkbox = page.get_by_text("Bookingimport")

        self.bookingdk_checkbox = page.get_by_text("Booking.dk")

        self.bookingse_checkbox = page.get_by_text("Booking.se")

        self.send_button = page.get_by_role(
            "button",
            name="Send"
        )

    def click_home(self):
        self.home_button.click()
        print("Home clicked")

    def click_email(self):
        self.email_button.click()
        print("Email clicked")

    def create_email_list(self, title, emails):

        self.create_email_list_button.click()

        print("Opening Create Email List popup")

        self.page.wait_for_timeout(2000)

        self.title_input.fill(str(title))

        self.emails_input.fill(str(emails))

        print("Title:", title)
        print("Emails:", emails)

        self.page.wait_for_timeout(2000)

        self.create_button.click()

        print("Create button clicked")

        self.page.wait_for_timeout(5000)

    def send_email(self, email_list, content):

        # Select Email List
        self.email_list_dropdown.click()

        self.email_list_dropdown.fill(str(email_list))

        self.page.wait_for_timeout(2000)

        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Content
        self.content_box.fill(str(content))

        # Check all boxes
        self.custom_checkbox.click()

        self.bookingimport_checkbox.click()

        self.bookingdk_checkbox.click()

        self.bookingse_checkbox.click()

        print("Email List:", email_list)
        print("Content:", content)

        self.page.wait_for_timeout(2000)

        self.send_button.click()

        print("Send button clicked")