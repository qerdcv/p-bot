import logging
import random
import time

from datetime import datetime
from threading import Thread

from telegram import Bot

from src import db
from config import get_phrases


log = logging.getLogger(__name__)


def send_result_messages(bot: Bot, chat_id, winner: db.User):
    phrases = get_phrases()
    response_phrases = random.choice(phrases.intermediate)
    response_phrase = random.choice(phrases.result)
    for phrase in response_phrases:
        bot.send_message(chat_id, phrase)
        time.sleep(3)
    bot.send_message(chat_id, response_phrase.format(winner.username))


def trigger_chat(chat_id: int, bot: Bot):
    chat_stat = db.get_chat(chat_id)
    phrases = get_phrases()
    if chat_stat is None:
        log.info('Create chat')
        db.create_chat(chat_id)
    else:
        # is last trigger was more than one day ago
        if not (datetime.utcnow() - chat_stat.modified_at).days:
            bot.send_message(
                chat_id,
                phrases.already_choice.format(chat_stat.last_choice)
            )
            return
    registered_users = db.get_registered_users(chat_id)
    winner = random.choice(registered_users)
    db.update_chat_winner(chat_id, winner.username)
    db.create_user_stat(chat_id, winner)
    # TODO: looks like shit. Rewrite with asyncio
    thread = Thread(target=send_result_messages, args=(bot, chat_id, winner))
    thread.start()
