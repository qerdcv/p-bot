import logging
import sqlite3

from datetime import datetime
from dataclasses import dataclass
from typing import (
    List,
    Optional,
)

from config import BASE_DIR

log = logging.getLogger(__name__)

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
DB_NAME = str(BASE_DIR / 'db' / 'p.db')
#  TODO: implements with sqlalchemy


@dataclass
class User:
    user_id: int
    username: str
    selected_count: Optional[int]


@dataclass
class UsersStat:
    users: List[User]
    in_game_cnt: int


@dataclass
class ChatStat:
    modified_at: datetime
    last_choice: Optional[str]


def get_date() -> str:
    return datetime.utcnow().strftime(DATE_FORMAT)


def parse_date(date: str) -> datetime:
    return datetime.strptime(date, DATE_FORMAT)


def get_query(query_name: str) -> str:
    try:
        with open(BASE_DIR / f'queries/{query_name}.sql', 'r') as f:
            return f.read()
    except FileNotFoundError:
        log.info(f'Query {query_name} not found')
        return ''


def create_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.executescript(get_query('init'))
        conn.commit()
        cursor.close()


def get_users_stat(chat_id: int) -> UsersStat:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        result = cursor.execute(
            get_query('get_users_stat'),
            (chat_id, )
        ).fetchall()
        cursor.close()
    users = []
    if result is not None:
        count = get_registered_count(chat_id)
        return UsersStat(
            [User(*row) for row in result],
            count
        )
    return UsersStat(users, 0)


def get_user(chat_id: int, user_id: int) -> Optional[User]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        result = cursor.execute(
            get_query('get_user'),
            (chat_id, user_id)
        ).fetchone()
        cursor.close()
    if result is not None:
        return User(**result)
    return result


def register_user(chat_id: int, user_id: int, username: str):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            get_query('register_user'),
            (
                chat_id,
                user_id,
                username,
                get_date()
            )
        )
        conn.commit()
        cursor.close()


def get_registered_count(chat_id: int) -> int:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        count, = cursor.execute(
            get_query('registered_count'), (chat_id, )
        ).fetchone()
        cursor.close()
    return count


def get_chat(chat_id: int) -> Optional[ChatStat]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        result = cursor.execute(
            get_query('get_chat'), (chat_id, )
        ).fetchone()
        cursor.close()
    if result is not None:
        modified_at, last_choice = result
        return ChatStat(
            modified_at=parse_date(modified_at),
            last_choice=last_choice
        )
    return result


def create_chat(chat_id: int):
    log.info(f'create chat {chat_id}')
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            get_query('create_chat'),
            (chat_id, get_date())
        )
        conn.commit()
        cursor.close()


def get_registered_users(chat_id: int) -> List[User]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        rows = cursor.execute(
            get_query('get_registered_users'),
            (chat_id, )
        ).fetchall()
        cursor.close()

    return [
        User(user_id, username, None)
        for user_id, username in rows
    ]


def update_chat_winner(chat_id: int, username: str):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            get_query('update_chat_winner'),
            (get_date(), username, chat_id)
        )
        cursor.close()


def create_user_stat(chat_id, user: User):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            get_query('create_user_stat'),
            (
                chat_id,
                user.user_id,
                get_date(),
                user.username
            )
        )
        cursor.close()


def switch_scheduler(chat_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(get_query('schedule_chat'), (chat_id, ))
        cursor.close()


def get_in_game_chats() -> List[int]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        rows = cursor.execute(get_query('get_in_game_chats')).fetchall()
        cursor.close()

    if rows is None:
        return []
    return [chat_id for (chat_id, ) in rows]
