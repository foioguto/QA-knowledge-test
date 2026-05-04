def validate_pet_response(body: dict, expected_id: int) -> None:
    assert body["id"] == expected_id
    assert body["name"]
    assert body["status"] in {"available", "pending", "sold"}
    