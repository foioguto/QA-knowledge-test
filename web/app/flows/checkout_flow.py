from web.app.infra.pages.cart_page import CartPage
from web.app.infra.pages.checkout_complete_page import CheckoutCompletePage
from web.app.infra.pages.checkout_overview_page import CheckoutOverviewPage
from web.app.infra.pages.checkout_page import CheckoutPage
from web.app.infra.pages.inventory_page import InventoryPage
from web.app.infra.pages.login_page import LoginPage


class CheckoutFlow:
    def __init__(self, driver) -> None:
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.checkout_overview_page = CheckoutOverviewPage(driver)
        self.checkout_complete_page = CheckoutCompletePage(driver)


    def execute(self, username: str, password: str) -> str:
        self.login_page.load()
        self.login_page.login(username, password)
        self.inventory_page.add_default_products()
        self.inventory_page.open_cart()
        self.cart_page.go_to_checkout()
        self.checkout_page.fill_checkout_form("debt augmenter", "CEO at Student", " 070.680.938-68")
        self.checkout_overview_page.finish_purchase()
        return self.checkout_complete_page.success_message()
