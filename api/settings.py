from dataclasses import dataclass
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).parent.parent.absolute()


class Settings:

    def __init__(self, settings):
        self.pg_config: PgConfig = PgConfig(**settings.get('postgres'))

    @classmethod
    def setup_from_file(cls, config_path: Path) -> 'Settings':
        with open(config_path) as f:
            config = yaml.safe_load(f)
            return cls(config)


@dataclass
class PgConfig:
    host: str
    port: int
    username: str
    password: str
    database_name: str
    min_pg_pool_size: int
    max_pg_pool_size: int
