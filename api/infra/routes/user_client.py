from urllib.parse import quote

from .base_client import BaseClient


class UserClient(BaseClient):
    def create_user(self, payload: dict):
        return self.post("/user", json=payload)


    def create_users_with_list_input(self, payload: dict):
        return self.post("/user/createWithList", json=payload)

    def create_users_with_array_input(self, payload: dict):
        return self.post("/user/createWithArray", json=payload)


    def get_user_login(self, username: str, password: str):
        return self.get(
            "/user/login",
            params={"username": username, "password": password},
        )


    def get_user_logout(self):
        return self.get("/user/logout")


    def get_user(self, username: str):
        return self.get(f"/user/{quote(username, safe='')}")


    def update_user(self, username: str, payload: dict):
        return self.put(f"/user/{quote(username, safe='')}", json=payload)


    def delete_user(self, username: str):
        return self.delete(f"/user/{quote(username, safe='')}")
