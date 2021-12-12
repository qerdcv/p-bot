import random

from src import db


def test_get_user():
    chat_id = random.randrange(100000)
    user_id = random.randrange(100000)
    username = 'test_user'

    user = db.get_user(chat_id, user_id)
    assert user is None

    db.register_user(chat_id, user_id, username)

    user = db.get_user(chat_id, user_id)
    assert user is not None
    assert user.user_id == user_id
    assert user.username == username
