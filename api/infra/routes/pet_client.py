from .base_client import BaseClient


class PetClient(BaseClient):
    def create_pet(self, payload: dict):
        return self.post("/pet", json=payload)
    

    def add_pet_photo(self, pet_id: int, file, additional_metadata: str | None = None):
        data = {}
        if additional_metadata is not None:
            data["additionalMetadata"] = additional_metadata

        return self.post(f"/pet/{pet_id}/uploadImage", files={"file": file}, data=data)


    def update_pet_status(self, payload: dict):
        return self.put("/pet", json=payload)
    

    def post_pet_status(self, pet_id: int, payload: dict):
        return self.post(f"/pet/{pet_id}", data=payload)


    def get_pet(self, pet_id: int):
        return self.get(f"/pet/{pet_id}")


    def update_pet(self, payload: dict):
        return self.put("/pet", json=payload)


    def delete_pet(self, pet_id: int):
        return self.delete(f"/pet/{pet_id}")
