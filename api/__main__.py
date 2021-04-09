import logging
import os
from aiohttp import web
from api.app import WorkWithFile, Token
from asyncpgsa import pg


def main():
    logging.basicConfig(level=logging.INFO)
    if not os.path.exists('./store'):
        os.mkdir('./store')
    app = web.Application()
    app.router.add_view('/', WorkWithFile)
    app.router.add_view('/token', Token)
    web.run_app(app)


if __name__ == '__main__':
    main()
