from selenium.webdriver.common.by import By

from web.app.infra.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")


    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.type(*self.FIRST_NAME, text=first_name)
        self.type(*self.LAST_NAME, text=last_name)
        self.type(*self.POSTAL_CODE, text=postal_code)
        self.click(*self.CONTINUE_BUTTON)
