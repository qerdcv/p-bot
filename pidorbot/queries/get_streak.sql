SELECT username, max(current_streak) AS max_streak, (
    select current_streak from p_stat where p.user_id=? order by id DESC
) as current_streak
FROM p_stat as p
WHERE chat_id=?
GROUP BY username;
