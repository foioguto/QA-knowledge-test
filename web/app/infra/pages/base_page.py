from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from web.app.infra.browser.wait_utils import wait


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver


    def open(self, url: str) -> None:
        self.driver.get(url)


    def click(self, by: By, value: str) -> None:
        wait(self.driver).until(ec.element_to_be_clickable((by, value))).click()


    def type(self, by: By, value: str, text: str) -> None:
        element = wait(self.driver).until(ec.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)


    def text_of(self, by: By, value: str) -> str:
        return wait(self.driver).until(ec.visibility_of_element_located((by, value))).text
    