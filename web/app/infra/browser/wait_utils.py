from selenium.webdriver.support.ui import WebDriverWait


def wait(driver, timeout: int = 10) -> WebDriverWait:
    return WebDriverWait(driver, timeout)
