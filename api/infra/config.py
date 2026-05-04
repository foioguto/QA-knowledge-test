import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class ApiConfig:
    base_url: str = field(
        default_factory=lambda: os.getenv("BASE_URL")
    )


api_config = ApiConfig()
