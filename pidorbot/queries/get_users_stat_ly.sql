SELECT user_id, username, count(user_id) AS count FROM p_stat
WHERE chat_id=?
  AND cast(strftime('%Y', choice_date) AS INTEGER) == DATE() - 1
GROUP BY user_id ORDER BY count DESC LIMIT 10;
