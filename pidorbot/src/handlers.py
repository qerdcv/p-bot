import logging
import shutil
import os
import requests
import telegram
from telegram import Update
from telegram.ext import CallbackContext

from src import db, tasks
from config import get_phrases
from client.config import BASE_PATH

log = logging.getLogger(__name__)


def parse_username(upd: Update) -> str:
    from_user = upd.message.from_user
    username = from_user.username
    if username is None:
        username = f'{from_user.first_name} {from_user.last_name}'
    else:
        username = f'@{username}'
    return username


def registration(upd: Update, ctx: CallbackContext):
    chat_id = upd.message.chat_id
    user_id = upd.message.from_user.id
    username = parse_username(upd)
    user = db.get_user(chat_id, user_id)
    phrases = get_phrases()
    if user is not None:
        ctx.bot.send_message(chat_id, phrases.already_registered)
        return
    photos = upd.message.from_user.get_profile_photos()
    photo_path = BASE_PATH / 'media' / f'{upd.message.from_user.id}.jpg'
    if not os.path.isfile(photo_path) and photos:
        response = requests.get(
            ctx.bot.get_file(
                upd.message.from_user.get_profile_photos().photos.pop().pop()
                .file_id
            )['file_path'], stream=True)
        with open(photo_path, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
    db.register_user(chat_id, user_id, username)
    ctx.bot.send_message(chat_id, phrases.registered)


def game(upd: Update, ctx: CallbackContext):
    chat_id = upd.message.chat_id
    phrases = get_phrases()
    reg_count = db.get_registered_count(chat_id)
    if reg_count == 0:
        ctx.bot.send_message(
            chat_id,
            phrases.no_registered.format(parse_username(upd))
        )
    elif reg_count == 1:
        ctx.bot.send_message(chat_id, phrases.not_enough_registered)
    else:
        tasks.trigger_chat(chat_id, ctx.bot)


def stat(upd: Update, ctx: CallbackContext):
    chat_id = upd.message.chat_id
    chat_stat = db.get_users_stat(upd.message.chat_id)
    phrases = get_phrases()
    if len(chat_stat.users) == 0:
        ctx.bot.send_message(
            chat_id,
            text=phrases.no_statistic.format(parse_username(upd)),
            parse_mode=telegram.ParseMode.HTML
        )
        return
    result = "Топ-10 <b>пидоров</b> за текущий год:\n\n"
    for i, user in enumerate(chat_stat.users):
        result += (
            f'{i + 1}. {user.username[1:]} - {user.selected_count} раз(а)\n'
        )
    result += f'\nВсего участников - {chat_stat.in_game_cnt}'
    ctx.bot.send_message(
        chat_id,
        text=result,
        parse_mode=telegram.ParseMode.HTML
    )


def ping(upd: Update, ctx: CallbackContext):
    ctx.bot.send_message(
        upd.message.chat_id,
        text="pong",
        reply_to_message_id=upd.message.message_id
    )


def schedule_chat(upd: Update, ctx: CallbackContext):
    chat_id = upd.message.chat_id
    reg_count = db.get_registered_count(chat_id)
    phrases = get_phrases()
    if reg_count < 2:
        ctx.bot.send_message(chat_id, phrases.not_enough_registered)
    db.switch_scheduler(chat_id)
    ctx.bot.send_message(chat_id, 'Ok...')
