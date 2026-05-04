from time import time


def build_pet_payload() -> dict:
    pet_id = int(time() * 1000)
    return {
        "id": pet_id,
        "category": {"id": 1, "name": "dogs"},
        "name": f"dog-{pet_id}",
        "photoUrls": ["./dog_photo.jpeg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available",
    }
