import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class ApiConfig:
    base_url: str = field(
        default_factory=lambda: os.environ.get("BASE_URL")
    )


api_config = ApiConfig()
