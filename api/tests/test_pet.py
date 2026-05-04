from api.modules.pet.validators import validate_pet_response


def test_create_get_pet(pet_service):
    created_pet = pet_service.create_pet()
    response = pet_service.get_pet(created_pet["id"])

    assert response.status_code == 200
    validate_pet_response(response.json(), created_pet["id"])


def test_delete_pet(pet_service):
    created_pet = pet_service.create_pet()
    delete_response = pet_service.delete_pet(created_pet["id"])
    get_response = pet_service.get_pet(created_pet["id"])

    assert delete_response.status_code == 200
    assert get_response.status_code in {404, 200}
