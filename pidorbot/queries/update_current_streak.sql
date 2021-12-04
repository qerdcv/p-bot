update main.p_users
set
    current_streak=?
where
    user_id=? AND chat_id=?
