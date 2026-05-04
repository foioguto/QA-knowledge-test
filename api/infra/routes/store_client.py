from .base_client import BaseClient


class StoreClient(BaseClient):
    def get_store_inventory(self):
        return self.get("/store/inventory")
    

    def get_store_order(self, order_id: int):
        return self.get(f"/store/order/{order_id}")


    def create_store_order(self, payload: dict):
        return self.post("/store/order", json=payload)


    def update_store_order(self, payload: dict):
        return self.create_store_order(payload)


    def delete_store_order(self, order_id: int):
        return self.delete(f"/store/order/{order_id}")
