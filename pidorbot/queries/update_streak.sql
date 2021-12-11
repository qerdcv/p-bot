UPDATE p_stat
SET
    current_streak=?
WHERE
    user_id=? AND
      (chat_id=? AND id=(select max(id) from p_stat where chat_id=?))
