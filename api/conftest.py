import pytest

from api.app.pet_service import PetService
from api.app.store_service import StoreService
from api.app.user_service import UserService
from api.infra.config import api_config
from api.infra.routes.pet_client import PetClient
from api.infra.routes.store_client import StoreClient
from api.infra.routes.user_client import UserClient


@pytest.fixture
def pet_service():
    return PetService(PetClient(api_config.base_url))


@pytest.fixture
def store_service():
    return StoreService(StoreClient(api_config.base_url))


@pytest.fixture
def user_service():
    return UserService(UserClient(api_config.base_url))
