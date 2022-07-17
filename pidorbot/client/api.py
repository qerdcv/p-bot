from enum import Enum
from aiohttp import web

from src import db


async def ping(request):
    return web.json_response({'message': 'pong'})


class FilterEnum(Enum):
    year = 'year'
    last_year = 'last_year'
    all_time = 'all_time'


async def get_users(request: web.Request) -> web.Response:
    active_filter = request.query.get('filter')
    if active_filter not in FilterEnum.__members__:
        active_filter = 'year'
    chat_id = request.match_info.get('chat_id')
    chat_stat = db.get_users_stat(chat_id, FilterEnum[active_filter])
    if chat_stat is None:
        return web.json_response({'message': 'chat not found'}, status=404)
    return web.json_response(chat_stat.to_dict())
