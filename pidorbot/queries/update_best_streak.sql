update main.p_users
set
    date_record=?,
    best_streak=?
where
    user_id=? AND chat_id=?
