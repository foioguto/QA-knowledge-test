from api.modules.store.validators import validate_order_response


def test_create_get_order(pet_service, store_service):
    created_pet = pet_service.create_pet()
    created_order = store_service.create_order(created_pet["id"])

    response = store_service.get_order(created_order["id"])

    assert response.status_code == 200
    validate_order_response(response.json(), created_order["id"])


def test_get_inventory(store_service):
    response = store_service.get_inventory()

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
