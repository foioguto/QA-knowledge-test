from time import time


def build_order_payload(pet_id: int) -> dict:
    order_id = int(time() * 1000)
    return {
        "id": order_id,
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2026-05-02T10:00:00.000Z",
        "status": "placed",
        "complete": True,
    }
