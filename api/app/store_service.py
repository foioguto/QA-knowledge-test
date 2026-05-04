from api.modules.store.payloads import build_order_payload
from api.infra.routes.store_client import StoreClient


class StoreService:
    def __init__(self, client: StoreClient) -> None:
        self.client = client


    def create_order(self, pet_id: int) -> dict:
        payload = build_order_payload(pet_id)
        response = self.client.create_store_order(payload)
        assert response.status_code == 200
        return response.json()


    def get_order(self, order_id: int):
        return self.client.get_store_order(order_id)


    def delete_order(self, order_id: int):
        return self.client.delete_store_order(order_id)


    def get_inventory(self):
        return self.client.get_store_inventory()
    
