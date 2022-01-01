SELECT user_id, username, count(user_id) AS count FROM p_stat
WHERE chat_id=?
GROUP BY user_id ORDER BY count DESC LIMIT 10;
