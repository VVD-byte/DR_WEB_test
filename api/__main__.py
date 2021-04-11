import logging
import os
from pathlib import Path

from aiohttp import web
from api.views import WorkWithFile, Token
from asyncpgsa import pg

from api.settings import Settings, BASE_DIR
from api.signals import pg_cleanup_context, db_controller_context


def main():
    logging.basicConfig(level=logging.INFO)
    if not os.path.exists('../store'):
        os.mkdir('../store')

    app = web.Application()

    config_path = Path(BASE_DIR.joinpath('config.yml'))
    config = Settings.setup_from_file(config_path)
    app['config'] = config

    app.router.add_view('/', WorkWithFile)
    app.router.add_view('/token', Token)
    app.cleanup_ctx.append(pg_cleanup_context)
    app.cleanup_ctx.append(db_controller_context)
    web.run_app(app)


if __name__ == '__main__':
    main()
