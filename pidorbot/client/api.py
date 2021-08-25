import aiohttp_jinja2
from aiohttp import web

from client.config import BASE_PATH
from src import db


async def ping(request):
    return web.json_response({'message': 'pong'})


async def media(request):
    with open(BASE_PATH / 'media' / request.match_info['file_name'], 'rb') as f:
        return web.Response(body=f.read(), content_type='image/jpg')


@aiohttp_jinja2.template('index.jinja2')
async def index(request: web.Request):
    chat_id = request.match_info.get('chat_id')
    chat_stat = db.get_users_stat(chat_id)
    return {
        'chat_id': request.match_info.get('chat_id'),
        'chat_stat': chat_stat
    }
