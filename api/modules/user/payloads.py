from time import time


def build_user_payload() -> dict:
    suffix = str(int(time() * 1000))
    return {
        "id": int(suffix),
        "username": f"user_{suffix}",
        "firstName": "QA",
        "lastName": "Student",
        "email": f"qa_{suffix}@mail.com",
        "password": "Secret123!",
        "phone": "81999999999",
        "userStatus": 1,
    }
