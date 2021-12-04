import aiohttp_jinja2
import jinja2
from aiohttp import web

from client.config import BASE_PATH
from client.routes import routes


def create_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app


def run():
    app = create_app()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(BASE_PATH / 'templates')
    )
    app['static_root_url'] = '/static'
    web.run_app(host='127.0.0.1', port=4444, app=app)
