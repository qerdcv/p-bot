from src import db


def pytest_sessionstart(session):
    db.create_database()


def pytest_sessionfinish(session):
    db.remove_database()
