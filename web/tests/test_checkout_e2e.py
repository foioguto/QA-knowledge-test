from web.app.flows.checkout_flow import CheckoutFlow


def test_complete_purchase(driver):
    flow = CheckoutFlow(driver)
    message = flow.execute("standard_user", "secret_sauce")

    assert message == "Thank you for your order!"
    