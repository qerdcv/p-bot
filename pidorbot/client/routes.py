from aiohttp import web
from client.config import BASE_PATH
from client import handlers
from client import api

routes = [
    web.get('/{chat_id}', handlers.index),
    web.get('/media/{file_name}', handlers.media),
    web.static('/static', BASE_PATH / 'static'),

    web.get('/api/ping', api.ping),
    web.get('/api/get-users/{chat_id}', api.get_users)
]
