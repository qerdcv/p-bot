from src import db


# TODO: refactor
def update_streak(chat_id: int, chat_stat: db.ChatStat, winner: db.User):
    if chat_stat is None:
        best_streak = 1
        db.update_streak(chat_id=chat_id, user_id=winner.user_id, current_streak=best_streak)
    else:
        best_streak = 0
        user_id = db.get_user_id(chat_id, chat_stat.last_choice)
        streak = db.get_streak(chat_id, winner.user_id)
        if user_id == winner.user_id:
            db.update_streak(chat_id, winner.user_id, current_streak=streak.current_streak + 1)
            streak = streak.current_streak + 1
            if db.is_best_streak(chat_id=chat_id, user_id=winner.user_id, current_streak=streak):
                best_streak = streak
        else:
            db.update_streak(chat_id, winner.user_id, 1)
            if streak.best_streak == 0:
                best_streak = 1
    return best_streak
