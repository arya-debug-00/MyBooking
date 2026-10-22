import allure
 
class AllureUtils:
 
    @staticmethod
    def attach_screenshot(page, name="Screenshot"):
        allure.attach(
            page.screenshot(full_page=True),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
 
    @staticmethod
    def attach_text(title, message):
        allure.attach(
            str(message),
            name=title,
            attachment_type=allure.attachment_type.TEXT
        )
 