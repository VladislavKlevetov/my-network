import logging
from aiohttp import web

from config.common import BaseConfig
from routes.base import setup_routes

def main():
    app = web.Application()
    setup_routes(app)
    app['config'] = BaseConfig
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)

if __name__ == '__main__':
    main()
