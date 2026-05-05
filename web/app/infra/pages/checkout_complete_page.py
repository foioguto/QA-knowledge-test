from selenium.webdriver.common.by import By

from web.app.infra.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def success_message(self) -> str:
        return self.text_of(*self.COMPLETE_HEADER)
    