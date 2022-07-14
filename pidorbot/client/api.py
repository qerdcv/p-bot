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
    active_filter = FilterEnum[active_filter]
    chat_id = request.match_info.get('chat_id')
    if active_filter == FilterEnum.year:
        chat_stat = db.get_users_stat(chat_id)
    elif active_filter == FilterEnum.last_year:
        chat_stat = db.get_users_stat_ly(chat_id)
    else:
        chat_stat = db.get_users_stat_at(chat_id)
    if chat_stat is None:
        return web.json_response({'message': 'chat not found'}, status=404)
    return web.json_response(chat_stat.to_dict())
