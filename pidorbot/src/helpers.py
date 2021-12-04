from src import db


# TODO: refactor
def update_streak(chat_id: int, chat_stat: db.ChatStat, winner: db.User):
    if chat_stat is None:
        best_streak = 1
        db.update_user_streak(chat_id, winner.user_id, streak=False)
        db.update_user_best_streak(chat_id, winner.user_id, best_streak)
    else:
        user_id = db.get_user_id(chat_id, chat_stat.last_choice)
        best_streak = 0
        if user_id == winner.user_id:
            db.update_user_streak(chat_id, winner.user_id, streak=True)
            streak = db.get_user_streak(chat_id, user_id)
            if streak.best_streak < streak.current_streak:
                best_streak = streak.current_streak
                db.update_user_best_streak(chat_id, winner.user_id, best_streak)
        else:
            db.update_user_streak(chat_id, winner.user_id, streak=False)
            streak = db.get_user_streak(chat_id, winner.user_id)
            if streak.best_streak == 0:
                best_streak = 1
                db.update_user_best_streak(chat_id, winner.user_id, best_streak)
    return best_streak
