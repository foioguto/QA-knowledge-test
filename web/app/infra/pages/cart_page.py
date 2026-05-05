from selenium.webdriver.common.by import By

from web.app.infra.pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")


    def go_to_checkout(self) -> None:
        self.click(*self.CHECKOUT_BUTTON)
        