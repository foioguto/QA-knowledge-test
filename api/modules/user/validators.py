def validate_user_response(body: dict, expected_username: str) -> None:
    assert body["username"] == expected_username
    assert body["email"]
    assert body["firstName"] == "QA"
