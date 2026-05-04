from api.modules.user.payloads import build_user_payload
from api.infra.routes.user_client import UserClient


class UserService:
    def __init__(self, client: UserClient) -> None:
        self.client = client


    def create_user(self) -> dict:
        payload = build_user_payload()
        response = self.client.create_user(payload)
        assert response.status_code == 200
        return response.json()


    def get_user(self, username: str):
        return self.client.get_user(username)


    def update_user(self, username: str, payload: dict):
        return self.client.update_user(username, payload)


    def delete_user(self, username: str):
        return self.client.delete_user(username)


    def login(self, username: str, password: str):
        return self.client.get_user_login(username, password)


    def logout(self):
        return self.client.get_user_logout()
    
