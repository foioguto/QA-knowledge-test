from api.modules.user.validators import validate_user_response


def test_create_get_user(user_service):
    created_user = user_service.create_user()
    response = user_service.get_user(created_user["username"])

    assert response.status_code == 200
    validate_user_response(response.json(), created_user["username"])


def test_update_user(user_service):
    created_user = user_service.create_user()
    created_user["firstName"] = "Updated"

    update_response = user_service.update_user(created_user["username"], created_user)
    get_response = user_service.get_user(created_user["username"])

    assert update_response.status_code == 200
    assert get_response.status_code == 200
    assert get_response.json()["firstName"] == "Updated"
    