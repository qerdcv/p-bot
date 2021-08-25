from aiohttp import web
from client.config import BASE_PATH
from client import api

routes = [
    web.get('/ping', api.ping),
    web.get('/{chat_id}', api.index),
    web.get('/media/{file_name}', api.media),
    web.static('/static', BASE_PATH / 'static')
]
