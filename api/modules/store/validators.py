def validate_order_response(body: dict, expected_order_id: int) -> None:
    assert body["id"] == expected_order_id
    assert body["quantity"] >= 1
    assert body["status"] in {"placed", "approved", "delivered"}
