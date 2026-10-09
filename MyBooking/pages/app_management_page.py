from playwright.sync_api import Page

class ApplicationManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.application_management_tab = page.locator("a").nth(5)
        self.edi_filter_tab = page.locator('xpath=//*[@id="root"]/div/div/div/div/div[3]/div/a[3]')

        # EDI Filter fields
        self.minimum_pallet_input = page.locator('input[name="minPallets"]')
        self.postal_code_input = page.locator('input[name="postalCode"]')
        self.customer_number_input = page.get_by_role("combobox")
        self.country_dropdown = page.locator('[role="button"][aria-haspopup="listbox"]').nth(0)
        self.edi_type_dropdown = page.locator('[role="button"][aria-haspopup="listbox"]').nth(1)
        self.note_input = page.locator('textarea[name="note"]')
        self.save_button = page.get_by_role("button", name="Save", exact=True)

    def click_application_management(self):
        self.application_management_tab.click()

    def click_edi_filter(self):
        print("EDI Filter found:", self.edi_filter_tab.count())
        self.edi_filter_tab.click()
        print("EDI Filter clicked")

    #EDI filter

    #edit
            
    def click_edit_by_note(self, note):
        record = self.page.locator("div.filterList").filter(has_text=note)
        record.locator("div.actionItems a").nth(0).click()

    def edit_edi_filter(self, edit_input):
        
        # Customer Number
        #self.customer_number_input.fill(str(edit_input["customerNumber"]))
        #self.page.wait_for_timeout(1000)
        #self.customer_number_input.press("ArrowDown")
        #self.customer_number_input.press("Enter")
        #self.page.wait_for_timeout(1000)
    
        # Postal Code
        self.postal_code_input.fill(str(edit_input["postalCode"]))
        self.page.wait_for_timeout(1000)
    
        # Country
        self.country_dropdown.click()
        self.page.keyboard.type(str(edit_input["country"]))
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1000)
    
        # EDI Type
        self.edi_type_dropdown.click()
        self.page.keyboard.type(str(edit_input["ediType"]))
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1000)

        # Minimum Pallets
        self.minimum_pallet_input.fill(str(edit_input["minPallets"]))
    
        # Note
        self.note_input.fill(str(edit_input["note"]))
        

        # Wait so you can check edited values
        self.page.wait_for_timeout(5000)
        
        # Save - keep commented for first test
        self.save_button.click()
        self.page.wait_for_timeout(5000)

    #delete
   # def click_edit_by_note(self, note):
       # note_element = self.page.get_by_text(note, exact=True)
       # record = note_element.locator("xpath=ancestor::div[contains(@class,'filterList')]")
       # record.locator("div.actionItems a").first.click()

    def create_edi_filter(self, test_input):
        self.minimum_pallet_input.fill(str(test_input["minPallets"]))
        self.customer_number_input.fill(str(test_input["customerNumber"]))
        self.page.wait_for_timeout(2000)
        #self.customer_number_input.press("ArrowDown")
        self.customer_number_input.press("Enter")
        self.page.wait_for_timeout(2000)
        print("Customer selected:", self.customer_number_input.locator("xpath=..").inner_text())
        self.postal_code_input.fill(str(test_input["postalCode"]))
        # Country
        self.country_dropdown.click()
        self.page.get_by_text("Sweden", exact=True).click()
    # EDI Type
        self.edi_type_dropdown.click()
        self.page.wait_for_timeout(1000)
        self.page.keyboard.type("Incoming check")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(5000)
        self.note_input.fill(str(test_input["note"]))
        print("Before Save - Note:", test_input["note"])
        print("Min pallets:", self.minimum_pallet_input.input_value())
        print("Postal code:", self.postal_code_input.input_value())
        print("Country:", self.country_dropdown.inner_text())
        print("EDI Type:", self.edi_type_dropdown.inner_text())
        print("Note:", self.note_input.input_value())
        self.page.wait_for_timeout(8000)
        print("Save buttons found:", self.save_button.count())
        self.save_button.click()
    
        #print("Save clicked")

        self.page.wait_for_timeout(5000)

        print(
            "Saved record found:",
            self.page.locator("div.filterList", has_text=str(test_input["note"])).count()
        )
            
