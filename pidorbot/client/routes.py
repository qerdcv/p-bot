from aiohttp import web
from client.config import BASE_PATH
from client import handlers

routes = [
    web.get('/ping', handlers.ping),
    web.get('/{chat_id}', handlers.index),
    web.get('/media/{file_name}', handlers.media),
    web.static('/static', BASE_PATH / 'static')
]
