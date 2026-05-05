from selenium.webdriver.common.by import By

from web.app.infra.pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_default_products(self) -> None:
        self.click(*self.ADD_BACKPACK)
        self.click(*self.ADD_BIKE_LIGHT)


    def open_cart(self) -> None:
        self.click(*self.CART_LINK)
