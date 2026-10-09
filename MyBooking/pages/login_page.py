import time
from playwright.sync_api import Page
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Login fields
        self.username_input = page.get_by_placeholder("Username")
        
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login", exact=True)
        # OTP Verify button
        self.verify_button = page.get_by_role("button", name="Verify", exact=True)
        # Menu & logout
        #self.menu_icon = page.get_by_test_id("MenuOutlinedIcon")
        #self.personIcon = page.get_by_test_id("PersonIcon")
        #self.logout = page.get_by_text("Logout")
        # Consignment locators
    
    def navigate(self):
        self.page.goto("https://internal.qa.bring.services/mybooking/user-login")

    def login(self, username, password):
        self.username_input.fill(username)
        print('Username entered')
        self.password_input.fill(password)
        print('Password entered')
        self.login_button.click()
        print('Login button clicked')
        time.sleep(2)

    def clickMenucIcon(self):
        self.menu_icon.click()
        print('Menu icon clicked')
        time.sleep(10)


    def verifylogout(self):
        # Wait for home title
        home_title = self.page.locator(self.home_text_locator).inner_text()
        assert home_title == "Home", f"Expected Home but got {home_title}"
        print('Home page verified')
        time.sleep(1)
        self.personIcon.click()
        self.logout.click()
        print('Logged out successfully')

    def get_error_message(self):
        return print("Error message placeholder")
