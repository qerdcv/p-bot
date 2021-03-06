from enum import Enum

import aiohttp_jinja2
from aiohttp import web

from client.config import BASE_PATH
from src import db


class FilterEnum(Enum):
    year = 'year'
    last_year = 'last_year'
    all_time = 'all_time'


async def ping(request):
    return web.json_response({'message': 'pong'})


async def media(request):
    with open(BASE_PATH / 'media' / request.match_info['file_name'], 'rb') as f:
        response = web.Response(body=f.read(), content_type='image/jpg')
        response.headers.update({
            'Cache-Control': 'max-age=86400',
        })
        return response


@aiohttp_jinja2.template('index.jinja2')
async def index(request: web.Request):
    active_filter = request.query.get('filter')
    if active_filter not in FilterEnum.__members__:
        active_filter = 'year'
    chat_id = request.match_info.get('chat_id')
    chat_stat = db.get_users_stat(chat_id, FilterEnum[active_filter])
    return {
        'chat_id': chat_id,
        'chat_stat': chat_stat,
        'active_filter': active_filter
    }
