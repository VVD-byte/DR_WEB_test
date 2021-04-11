import logging
from typing import Generator

from aiohttp.web_app import Application
from asyncpgsa import create_pool

from api.settings import Settings
from .schema import DBConnect


logger = logging.getLogger(__name__)


async def pg_cleanup_context(app: Application) -> Generator:
    config: Settings = app['config']
    pg_config = config.pg_config
    async with create_pool(
            host=pg_config.host,
            port=pg_config.port,
            database=pg_config.database_name,
            user=pg_config.username,
            password=pg_config.password,
            min_size=pg_config.min_pg_pool_size,
            max_size=pg_config.max_pg_pool_size
    ) as pool:
        app['postgres'] = pool
        yield


async def db_controller_context(app: Application):
    pg = app['postgres']
    db_controller = DBConnect(pg)
    app['db_controller'] = db_controller
    yield
