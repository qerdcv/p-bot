import os
import logging

from multiprocessing import Process

import telegram.ext

from telegram.ext import (
    Updater,
    CommandHandler,
)

from client.config import MEDIA_PATH
from client_main import run
from src.db import create_database
from src import handlers
from src.scheduler import run_scheduler, exit_event

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def setup_handlers(dispatcher: telegram.ext.Dispatcher):
    dispatcher.add_handler(CommandHandler('pstat', handlers.stat))
    dispatcher.add_handler(CommandHandler('reg', handlers.registration))
    dispatcher.add_handler(CommandHandler('play', handlers.game))
    dispatcher.add_handler(CommandHandler('schedule', handlers.schedule_chat))
    dispatcher.add_handler(CommandHandler('ping', handlers.ping))
    dispatcher.add_handler(CommandHandler('migrate', handlers.migrate))


def handle_exit(sig, frame):
    exit_event.set()


if __name__ == '__main__':
    create_database()
    MEDIA_PATH.mkdir(exist_ok=True)
    client_process = Process(target=run)
    client_process.start()
    #  Start client process

    updater = Updater(
        token=os.environ['BOT_TOKEN'],
        use_context=True,
        user_sig_handler=handle_exit
    )
    dispatcher = updater.dispatcher
    setup_handlers(dispatcher)
    run_scheduler(dispatcher.bot)
    updater.start_polling()
    updater.idle()
