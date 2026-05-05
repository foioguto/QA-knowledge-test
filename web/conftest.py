import pytest

from web.app.infra.browser.driver_factory import create_chrome_driver


@pytest.fixture
def driver():
    browser = create_chrome_driver()
    yield browser
    browser.quit()
