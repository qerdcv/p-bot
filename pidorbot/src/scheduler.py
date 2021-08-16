import threading
import time

import schedule
import telegram

from src import db
from src.tasks import trigger_chat

exit_event = threading.Event()


def scheduling(bot):

    def trigger_chats():
        in_game_chats = db.get_in_game_chats()
        for chat in in_game_chats:
            trigger_chat(chat, bot)

    schedule.every().day.at('07:00').do(trigger_chats)
    while not exit_event.is_set():
        schedule.run_pending()
        time.sleep(1)


def run_scheduler(bot: telegram.Bot):
    thread = threading.Thread(target=scheduling, args=(bot, ))
    thread.start()
