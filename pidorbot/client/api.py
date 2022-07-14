from enum import Enum
from aiohttp import web

from src import db


async def ping(request):
    return web.json_response({'message': 'pong'})


class FilterEnum(Enum):
    year = 'year'
    last_year = 'last_year'
    all_time = 'all_time'


async def get_users(request: web.Request):
    chat_id = request.match_info.get('chat_id')
    res = db.get_users_stat_at(chat_id)
    if res is None:
        return web.json_response({'message': 'chat not found'}, status=404)
    return web.json_response(res.to_dict())
