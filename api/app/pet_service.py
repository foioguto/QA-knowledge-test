from api.modules.pet.payloads import build_pet_payload
from api.infra.routes.pet_client import PetClient


class PetService:
    def __init__(self, client: PetClient) -> None:
        self.client = client


    def create_pet(self) -> dict:
        payload = build_pet_payload()
        response = self.client.create_pet(payload)
        assert response.status_code == 200
        return response.json()


    def get_pet(self, pet_id: int):
        return self.client.get_pet(pet_id)


    def delete_pet(self, pet_id: int):
        return self.client.delete_pet(pet_id)

    def update_pet(self, pet_id: int, payload: dict):
        updated_payload = payload.copy()
        updated_payload["id"] = pet_id
        return self.client.update_pet(updated_payload)
