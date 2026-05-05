from selenium.webdriver.common.by import By

from web.app.infra.pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def finish_purchase(self) -> None:
        self.click(*self.FINISH_BUTTON)